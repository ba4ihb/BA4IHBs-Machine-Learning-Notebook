#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf.py —— 把课程笔记本执行后导出为 PDF（中文/公式/图表正常，不裁边）
用法:
    python build_pdf.py nb1.ipynb [nb2.ipynb ...]
    python build_pdf.py --all
"""
import re, os, sys, glob, uuid, struct, base64, subprocess, tempfile
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter
from weasyprint import HTML

CJK_FONT = "Noto Sans CJK JP"   # XeLaTeX 渲染公式用的中文字体
DPI = 300

def to_lines(t):
    t = t.rstrip("\n"); L = [l + "\n" for l in t.split("\n")]
    if L: L[-1] = L[-1].rstrip("\n")
    return L

def png_size(path):
    with open(path, "rb") as f: d = f.read(24)
    return struct.unpack(">II", d[16:24])

def render_math(latex):
    d = tempfile.mkdtemp(); tex = os.path.join(d, "m.tex")
    with open(tex, "w", encoding="utf-8") as f:
        f.write("\\documentclass[border=2pt]{standalone}\n"
                "\\usepackage{amsmath}\n\\usepackage{fontspec}\n"
                "\\setmainfont{%s}\n\\begin{document}\n$\\displaystyle %s$\n\\end{document}\n"
                % (CJK_FONT, latex))
    subprocess.run(["xelatex","-interaction=nonstopmode","-halt-on-error","m.tex"],
                   cwd=d, capture_output=True)
    pdf, png = os.path.join(d,"m.pdf"), os.path.join(d,"m.png")
    if not os.path.exists(pdf): return None
    subprocess.run(["pdftoppm","-png","-r",str(DPI),"-singlefile",pdf,os.path.join(d,"m")],
                   capture_output=True)
    if not os.path.exists(png): return None
    w,_ = png_size(png)
    uri = "data:image/png;base64," + base64.b64encode(open(png,"rb").read()).decode()
    return uri, max(40, round(w*96.0/DPI))

def replace_display_math(src):
    def repl(m):
        got = render_math(m.group(1))
        if not got: return m.group(0)
        uri, wpx = got
        return ('<div style="text-align:center;margin:10px 0;">'
                '<img src="%s" style="width:%dpx;height:auto;max-width:100%%;"></div>' % (uri, wpx))
    return re.sub(r"\$\$(.+?)\$\$", repl, src, flags=re.S)

EMOJI = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U00002B00-\U00002BFF"
                   "\U0001F1E6-\U0001F1FF\U0000FE00-\U0000FE0F\u200d]+")

# 自己的一套干净样式（不再依赖 nbconvert 自带 CSS，避免它把内容撑宽裁边）
CSS = """<style>
@page { size: A4; margin: 1.4cm 1.2cm; }
*, *::before, *::after { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: "Noto Sans CJK JP","Microsoft YaHei","PingFang SC",sans-serif;
       font-size: 10.5pt; line-height: 1.65; color: #111; }
h1, h2, h3, h4 { font-weight: bold; line-height: 1.3; }
h1 { font-size: 19pt; margin: 0 0 6px; }
h2 { font-size: 15pt; border-bottom: 1.5px solid #ddd; padding-bottom: 3px; margin: 16px 0 8px; }
h3 { font-size: 12.5pt; margin: 12px 0 6px; }
p, li, blockquote { margin: 6px 0; }
.jp-Cell { margin: 0 0 6px; }
.jp-InputPrompt, .jp-OutputPrompt { color: #999; font-size: 8.5pt; }
pre { font-family: "DejaVu Sans Mono","Consolas",monospace; font-size: 9pt;
      white-space: pre-wrap; overflow-wrap: anywhere;
      border: 1px solid #e3e3e3; border-radius: 4px; padding: 6px 8px; margin: 6px 0;
      page-break-inside: avoid; }
div.highlight { margin: 6px 0; }
code { font-family: "DejaVu Sans Mono","Consolas",monospace; background: #f0f0f3;
       padding: 0 3px; border-radius: 3px; font-size: 9pt; }
table { border-collapse: collapse; font-size: 10pt; page-break-inside: avoid; margin: 8px 0; }
th, td { border: 1px solid #ccc; padding: 4px 8px; }
blockquote { border-left: 3px solid #ccc; padding: 2px 12px; color: #444;
             background: #fafafa; page-break-inside: avoid; }
img { max-width: 100%; height: auto; }
.anchor-link { display: none !important; }
.jp-OutputArea-child, .jp-OutputArea-output, .jp-RenderedImage { page-break-inside: avoid; }
/* 代码高亮（少量常用 token，保持可读） */
.highlight .k,.highlight .kn,.highlight .kd,.highlight .kc { color:#008; font-weight:bold; }
.highlight .s,.highlight .s1,.highlight .s2,.highlight .sb { color:#a11; }
.highlight .c,.highlight .c1,.highlight .cm { color:#888; font-style:italic; }
.highlight .mi,.highlight .mf,.highlight .m { color:#164; }
.highlight .nf,.highlight .nb { color:#06c; }
.highlight .o,.highlight .ow { color:#333; }
</style>"""

def convert(path, outdir):
    nb = nbformat.read(path, as_version=4)
    for c in nb.cells:
        if "id" not in c: c["id"] = uuid.uuid4().hex[:8]
        if c.cell_type == "markdown":
            src = "".join(c.source)
            if "$$" in src: src = replace_display_math(src)
            c.source = src
    ep = ExecutePreprocessor(timeout=300, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": os.path.dirname(path)}})
    html, _ = HTMLExporter().from_notebook_node(nb)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.S)   # 去掉 nbconvert 自带样式
    html = EMOJI.sub("", html)
    html = html.replace("</head>", CSS + "</head>")
    os.makedirs(outdir, exist_ok=True)
    name = os.path.splitext(os.path.basename(path))[0]
    pdf = os.path.join(outdir, name + ".pdf")
    HTML(string=html, base_url=os.path.dirname(path)).write_pdf(pdf)
    return pdf

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args == ["--all"]:
        d = os.getcwd()
        files = sorted(glob.glob(os.path.join(d, "第*课*.ipynb")) +
                       glob.glob(os.path.join(d, "*数学*.ipynb")))
    else:
        files = args
    outdir = os.path.join(os.path.dirname(os.path.abspath(files[0])), "pdf")
    for f in files:
        print("转换:", os.path.basename(f))
        print("   -> PDF:", os.path.basename(convert(f, outdir)))
    print("完成，输出目录:", outdir)
