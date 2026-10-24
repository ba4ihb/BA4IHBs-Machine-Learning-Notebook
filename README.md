# BA4IHB's Machine Learning Notebook

**从零开始学机器学习 · 可运行的 Jupyter Notebook + 配套 PDF**

这是一份「零基础」友好的中文学习笔记，跟着 Andrew Ng（吴恩达）的
[Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction-from-stanford-deeplearning-ai) 走。
每个知识点都做成了**能直接运行的笔记本**：先用大白话 + 生活类比讲清楚，再用代码跑一遍、画出图来「看得见」，最后附上作业。

> 适合谁：没学过机器学习、数学基础较弱、想动手跑起来的初学者。
> 不适合：只想看速成结论、不想动手的人。

---

## 📺 配套视频课程

| 语言 | 平台 | 链接 |
|---|---|---|
| 英文原版 | YouTube | [Machine Learning Specialization — Andrew Ng (deepLearning.AI)](https://www.youtube.com/watch?v=vStJoetOxJg&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI) |
| 官方中英字幕 | 哔哩哔哩 | [【官方中英】2025年公认最好的【吴恩达机器学习课程】](https://www.bilibili.com/video/BV1owrpYKEtP/) |

**学习方式（反转课堂）**：先看视频，再打开对应笔记本动手跑一遍。看不懂的地方就回来翻笔记里的图和代码。

---

## 🚀 环境安装

> 这一节是给「还没配好 Python 环境」的同学看的。如果你已经有了 Anaconda / conda 环境，可以跳到 [3. 打开笔记本](#3-打开笔记本)。

### 1. 安装 Python

- **最省事的方式（推荐）**：安装 **Anaconda** 或 **Miniconda**（自带 conda、Python、Jupyter）
  - 官方下载：<https://www.anaconda.com/download>
  - Windows 安装时勾选 **「Add to PATH」**（如果没勾也没关系，后面用绝对路径也行）
- **只装 Python 也可以**：去 <https://www.python.org/downloads/> 下载（勾选「Add Python to PATH」）
- **需要 NVIDIA GPU**：装好后用 `nvidia-smi` 看显卡驱动版本（后面装 PyTorch 会用到）

### 2. 安装 Python 库

打开「命令提示符」（Windows：`Win + R` → 输入 `cmd` → 回车）或 Anaconda Prompt。

```bash
# 创建一个干净的环境（conda 用户，推荐）
conda create -n ml python=3.11 -y
conda activate ml

# 纯 Python 用户跳过上面两步，直接开始装库

pip install jupyter numpy matplotlib scikit-learn pandas
```

**每个库是干什么的**（看不懂也没关系，先装上）：

| 库 | 用途 |
|---|---|
| `jupyter` | 运行 `.ipynb` 笔记本 |
| `numpy` | 数值计算（向量、矩阵） |
| `matplotlib` | 画图 |
| `scikit-learn` | 机器学习常用算法 |
| `pandas` | 处理表格数据 |

### 3. 安装 PyTorch（可选）

> **先说清楚**：本仓库目前的笔记**只用到 numpy + matplotlib**，学前 9 课完全不需要 PyTorch。
> 后面进入深度学习才用得到。想提前装的话按下面走。

1. 打开 PyTorch 官网选择器：<https://pytorch.org/get-started/locally/>
2. 按你的系统选（例如 Windows + CUDA 12.x + Python）
3. 复制官网给你的安装命令执行，例如：

```bash
# 有 NVIDIA GPU（CUDA 版本以官网为准）
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# 没有 GPU，只想跑通（CPU 版）
pip install torch torchvision torchaudio
```

4. **验证安装**（跑一段小代码看是不是成功）：

```python
import torch
print("PyTorch 版本：", torch.__version__)
print("GPU 可用：", torch.cuda.is_available())
```

**国内网络慢？** 用清华镜像装库：

```bash
pip install jupyter numpy matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 4. 打开笔记本

有三种方式，**选一种即可**：

**方式 A · Jupyter Notebook（最经典）**
```bash
cd notebooks/
jupyter notebook
```
浏览器会自动打开一个界面，点击 `.ipynb` 文件就能看。

**方式 B · VSCode（推荐）**
1. 下载安装 [VSCode](https://code.visualstudio.com/)
2. 安装扩展：**Jupyter**（扩展市场搜 `Jupyter`，作者 Microsoft）
3. 直接打开 `.ipynb` 文件 → 点右上角 **运行** / **Run All**
4. 也可以在 VSCode 里「打开终端」，先 `conda activate ml`（如果用 conda）再 `code .` 打开整个目录

**方式 C · JupyterLab**（介于两者之间，命令：`jupyter lab`）

> **提示**：Windows 上如果 `jupyter` 命令找不到，多半是 `pip` 装的脚本目录没加进 PATH，或者 Anaconda 的 Scripts 目录没加入 PATH。用 Anaconda Prompt 启动就行。

---

## 📚 目录

> 每个 `第N课` 对应 Coursera 课程里的一个小节（Lesson）。带 🔜 的是计划中，会陆续补上。

### Week 1 · 什么是机器学习 & 单变量线性回归

| 课 | 主题 | 笔记本 | PDF | 课程位置 |
|---|---|---|---|---|
| 第 1 课 | 什么是机器学习 | [ipynb](notebooks/第1课_什么是机器学习.ipynb) | [pdf](pdf/第1课_什么是机器学习.pdf) | W1 · L1 |
| 第 2 课 | 监督学习与无监督学习 | [ipynb](notebooks/第2课_监督学习与无监督学习.ipynb) | [pdf](pdf/第2课_监督学习与无监督学习.pdf) | W1 · L2 |
| 第 3 课 | 线性回归模型 | [ipynb](notebooks/第3课_线性回归模型.ipynb) | [pdf](pdf/第3课_线性回归模型.pdf) | W1 · L3 |
| 第 4 课 | 成本函数 | [ipynb](notebooks/第4课_成本函数.ipynb) | [pdf](pdf/第4课_成本函数.pdf) | W1 · L3 |
| 第 5 课 | 梯度下降 | [ipynb](notebooks/第5课_梯度下降.ipynb) | [pdf](pdf/第5课_梯度下降.pdf) | W1 · L4 |
| 第 6 课 | 梯度下降用于线性回归 | [ipynb](notebooks/第6课_梯度下降用于线性回归.ipynb) | [pdf](pdf/第6课_梯度下降用于线性回归.pdf) | W1 · L4 |

### Week 2 · 多元线性回归

| 课 | 主题 | 笔记本 | PDF | 课程位置 |
|---|---|---|---|---|
| 第 7 课 | 多元线性回归 | [ipynb](notebooks/第7课_多元线性回归.ipynb) | [pdf](pdf/第7课_多元线性回归.pdf) | W2 · L1 |
| 第 8 课 | 向量化 | [ipynb](notebooks/第8课_向量化.ipynb) | [pdf](pdf/第8课_向量化.pdf) | W2 · L1 |
| 第 9 课 | 多元梯度下降 | [ipynb](notebooks/第9课_多元梯度下降.ipynb) | [pdf](pdf/第9课_多元梯度下降.pdf) | W2 · L1 |
| 第 10 课 | 特征缩放 🔜 | — | — | W2 · L1 |
| 第 11 课 | 检查收敛与选择学习率 🔜 | — | — | W2 · L1 |
| 第 12 课 | 特征工程与多项式回归 🔜 | — | — | W2 · L1 |

### 配套数学（按需查阅，不用一次看完）

| 文件 | 内容 | 何时看 |
|---|---|---|
| [数学基础急救包](notebooks/数学基础急救包.ipynb) · [pdf](pdf/数学基础急救包.pdf) | 变量、函数、平方、求和 Σ、直线方程、下标记号 | 卡在基本符号时 |
| [数学补丁：导数与梯度](notebooks/数学补丁_导数与梯度.ipynb) · [pdf](pdf/数学补丁_导数与梯度.pdf) | 斜率、切线、导数、偏导数 ∂ | 学梯度下降（第 5 课）之前 |

---

## 💡 怎么用这份笔记

1. **先看视频**（YouTube 或 B 站），对应章节见目录里的「课程位置」。
2. **打开笔记本**，从上往下读；灰色代码格点一下，按 `Shift + Enter` 运行。
3. **看图找感觉**——每节课都有图，比公式管用。
4. **做课后作业**（每节课末尾），写在笔记本里或纸上。
5. **看不懂就翻配套数学**，或回看视频那几分钟。

**两个使用提示：**

- 笔记本里的图使用了中文字体自动选择（Windows 用微软雅黑、macOS 用苹方、Linux 用 Noto）。如果你的系统字体缺失，图中中文可能显示为方框，安装任意中文字体即可。
- `.ipynb` 需要在 Jupyter / VSCode 里打开，**不要**用文本编辑器直接编辑（会破坏格式）。

---

## 🗂 仓库结构

```
BA4IHB's Machine Learning Notebook/
├── README.md                    ← 你在这里
├── LICENSE                      ← MIT 许可证
├── .gitignore
├── notebooks/                   ← 每节课的 Jupyter Notebook
│   ├── 第1课_什么是机器学习.ipynb
│   ├── 第2课_监督学习与无监督学习.ipynb
│   ├── ...
│   ├── 第9课_多元梯度下降.ipynb
│   ├── 数学基础急救包.ipynb        ← 配套数学（按需查阅）
│   └── 数学补丁_导数与梯度.ipynb
├── pdf/                         ← 每节课的 PDF 版（不想开 Jupyter 时看）
│   └── 同上文件名.pdf
└── tools/
    └── build_pdf.py             ← 把 .ipynb 执行并导出成 PDF 的脚本
```

**PDF 是怎么来的？** 运行 `tools/build_pdf.py` 会执行每个笔记本（让代码跑出图），然后渲染成 PDF。它要求本机有 `jupyter nbconvert`、`weasyprint`、`pandoc`、`xelatex` 等工具，普通学习**不需要**——只在你想批量更新 PDF 时用。

```bash
# 需要提前装：pip install nbconvert weasyprint；系统还要有 xelatex
cd tools/
python build_pdf.py --all
```

---

## ❓ 常见问题

**Q：图里的中文变成方框了？**
A：系统缺少中文字体。安装任一中文字体（Windows 微软雅黑、macOS 苹方、Linux Noto），重新运行那一格。

**Q：代码报 `ModuleNotFoundError: No module named 'numpy'`？**
A：你用的 Python 环境没装库，执行 `pip install numpy matplotlib`（conda 用户记得 `conda activate ml` 先激活环境）。

**Q：`pip install` 报 `No matching distribution found`？**
A：十有八九是拼写错了库名（比如 `numy` 应为 `numpy`）。仔细看报错里那个库名拼写。

**Q：Jupyter 打开了，但代码跑不动/输出乱码？**
A：在 Jupyter 顶部菜单选择正确的 kernel（Python 3 / 你的 conda 环境）。乱码多是字体问题，见上。

**Q：PDF 里的数学公式显示为原始 LaTeX 代码？**
A：旧版 PDF 有这个问题，已修复。请重新下载最新 PDF；如果你自己生成，确保 `tools/build_pdf.py` 是最新版。

---

## 📄 License

[MIT](LICENSE)

---

**Happy Learning! 🎉**
