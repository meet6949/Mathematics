<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=Stats%20%26%20Linear%20Algebra&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=35&desc=A%20Statistics%20%26%20Linear%20Algebra%20Practical%20Exam%20on%20Student%20Score%20Data&descAlignY=55&descSize=17" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-4CB391?style=for-the-badge)](https://seaborn.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)](https://matplotlib.org)
[![Status](https://img.shields.io/badge/Status-Complete-22c55e?style=for-the-badge)]()
<br/>

> *✨ "Data is the new oil — but only if you know how to refine it." ✨*

<br/>

**⏱️ Duration:** 6 Hours &nbsp;&nbsp;**|**&nbsp;&nbsp; **🧪 Type:** Theory + Practical &nbsp;&nbsp;**|**&nbsp;&nbsp; **🏥 Domain:** Public Health Analytics

**👨‍💻 Author:** Meet Gajera
<br/>

</div>

---

## 📌 Table of Contents

<details open>
<summary><b>Click to expand / collapse</b></summary>

- [🎯 Project Overview](#-project-overview)
- [🗄️ Dataset Structure](#️-dataset-structure)
- [📚 Theoretical Foundation](#-theoretical-foundation-part-a)
- [🔬 Analysis Tasks](#-analysis-tasks-part-b)
- [✅ Results Summary](#-results-summary)
- [🚀 How to Run](#-how-to-run)
- [📁 File Structure](#-file-structure)
- [🧠 Key Concepts Quick Reference](#-key-concepts-quick-reference)

</details>

---

## 🎯 Project Overview

<table>
<tr>
<td>

You are a **data analyst examining real student exam records**. Armed with score data across Math, Science, and English subjects, your mission is to use the power of **statistics and linear algebra** to understand student performance — and *uncover the patterns* behind every mark scored.

**The data covers:**
- 📐 Math, Science & English exam scores
- ⏱️ Hours studied per student
- ✅ Pass / Fail classification

**The goal:** Compute measures of central tendency, fit distributions, apply probability, and use vector algebra to draw *data-driven insights* about student performance.

</td>
<td>

```
📦 Student Score Records
         │
         ▼
📊 Central Tendency & Dispersion
         │
         ▼
🎲 Probability Analysis
         │
         ▼
📈 Distribution & Visualization
         │
         ▼
🔢 Linear Algebra (Vectors)
         │
         ▼
✅ Key Insights
```

</td>
</tr>
</table>

---

## 🗄️ Dataset Structure

> **File:** `students_scores.csv` &nbsp;|&nbsp; **Features:** `5`

| # | Field Name | Data Type | Description |
|---|------------|-----------|-------------|
| 1 | `Math_Score` | Float | 📐 Student's mathematics exam score |
| 2 | `Science_Score` | Float | 🔬 Student's science exam score |
| 3 | `English_Score` | Float | 📖 Student's English exam score |
| 4 | `Hours_Studied` | Float | ⏱️ Total hours the student studied |
| 5 | `Pass_Fail` | Int | ✅ `1` = Pass · `0` = Fail |

---

## 📚 Theoretical Foundation (Part A)

> 💡 **4 Core Concepts** — detailed notes with formulas, properties, and project-specific applications.

<details>
<summary><b>1️⃣ Measures of Central Tendency</b> — The backbone of all analysis</summary>

<br/>

**Definition:** Central tendency describes where the "center" of a dataset lies — the most representative value.

```
Mean   = Σx / n
Median = Middle value when data is sorted
Mode   = Most frequently occurring value
```

**Key Parameters:**
| Measure | Best Used When | Sensitive to Outliers? |
|---|---|---|
| Mean (μ) | Symmetric data, no outliers | Yes |
| Median | Skewed data or outliers present | No |
| Mode | Categorical or discrete data | No |

> 📌 *In this project:* Applied to `Math_Score` to understand where most students cluster in performance.

<br/>
</details>

<details>
<summary><b>2️⃣ Measures of Dispersion</b> — Spread around the center</summary>

<br/>

**Definition:** Dispersion measures how spread out the data values are from the central value.

```
Range     = Max − Min
Variance  = Σ(xᵢ − μ)² / n
Std Dev   = √Variance
```

**How to interpret:**
- **Low std dev** → values are clustered near the mean
- **High std dev** → values are spread far from the mean
- **Range** gives total span but is sensitive to extreme values

> 📌 *In this project:* Applied to `Science_Score` to measure consistency of student performance across the class.

<br/>
</details>

<details>
<summary><b>3️⃣ Probability & Conditional Probability</b> — Likelihood of outcomes</summary>

<br/>

Models the likelihood of events from Pass/Fail data.

```
P(A)      = Favourable outcomes / Total outcomes

P(A | B)  = P(A ∩ B) / P(B)        ← Conditional Probability

Contingency Table:
         Hours > 5   Hours ≤ 5
Pass  |     a      |     b     |
Fail  |     c      |     d     |
```

> 📌 *In this project:* Computed **P(Pass)** overall and **P(Pass | Hours_Studied > 5)** using a contingency table — revealing the impact of study time on outcomes.

> 💡 If P(Pass | Hours > 5) >> P(Pass), then study hours and passing are **dependent events**.

<br/>
</details>

<details>
<summary><b>4️⃣ Normal Distribution & Visualization</b> — The bell curve</summary>

<br/>

A symmetric, bell-shaped distribution defined by mean μ and std dev σ.

```
PDF: f(x) = [1/(σ√2π)] × exp[−(x − μ)² / (2σ²)]

Empirical Rule:
  P(μ − σ  < X < μ + σ)  ≈ 68.3%
  P(μ − 2σ < X < μ + 2σ) ≈ 95.4%
  P(μ − 3σ < X < μ + 3σ) ≈ 99.7%
```

**Skewness & Kurtosis:**
| Metric | Formula | Interpretation |
|---|---|---|
| Skewness | Σ((xᵢ−μ)/σ)³ / n | 0 = symmetric; + = right tail; − = left tail |
| Kurtosis | Σ((xᵢ−μ)/σ)⁴ / n − 3 | 0 = normal; + = heavy tails; − = light tails |

> 📌 *In this project:* Histogram + Normal Curve for `Math_Score`; Skewness & Kurtosis for `Science_Score`; Q-Q Plot for `English_Score`.

<br/>
</details>

<details>
<summary><b>5️⃣ Q-Q Plot</b> — Normality testing without histograms</summary>

<br/>

**Definition:** A Quantile-Quantile plot compares two probability distributions by plotting their quantiles against each other.

**How to read it:**
- Points on the **45° diagonal line** → data follows that distribution ✓
- **Curved/bent tails** → skewness or heavy tails
- **S-shaped curve** → kurtosis mismatch

> 📌 *In this project:* Q-Q Plot of `English_Score` against a theoretical normal distribution checks whether scores are normally distributed.

<br/>
</details>

<details>
<summary><b>6️⃣ Linear Algebra — Vectors, Dot Product & Norms</b> — Geometry of scores</summary>

<br/>

Represent student scores as vectors in n-dimensional space.

```
Vector A = [Math scores of first 5 students]
Vector B = [Science scores of first 5 students]

Dot Product:   A · B = Σ(aᵢ × bᵢ)

Norm 1 (L1):  ||A||₁ = Σ|aᵢ|
Norm 2 (L2):  ||A||₂ = √(Σaᵢ²)    ← Euclidean length

Angle:  θ = cos⁻¹( A·B / (||A||₂ × ||B||₂) )
```

**Key Properties:**
- **Dot Product > 0** → vectors point in same direction (positive correlation)
- **Small angle θ** → high similarity between the two score profiles
- **Norm 2** is the most common measure of vector magnitude

> 📌 *In this project:* A small angle between Math and Science vectors confirms that students who perform well in one subject tend to perform well in the other.

<br/>
</details>

---

## 🔬 Analysis Tasks (Part B)

### 📋 Tasks Completed

- [x] 📂 Dataset loading & exploratory analysis
- [x] 📊 Mean, Median, Mode — `Math_Score`
- [x] 📏 Range, Variance, Standard Deviation — `Science_Score`
- [x] 🎲 P(Pass) — overall pass probability from `Pass_Fail`
- [x] 📋 Contingency Table — `Pass_Fail` vs `Hours_Studied > 5`
- [x] 🔗 Conditional Probability — P(Pass | Hours_Studied > 5)
- [x] 📈 Histogram + Normal Curve — `Math_Score`
- [x] 〰️ Skewness & Kurtosis — `Science_Score`
- [x] 📉 Q-Q Plot — `English_Score`
- [x] 🔢 Score Vectors — first 5 students' Math & Science scores
- [x] ✖️ Dot Product — Math vector · Science vector
- [x] 📐 Norm 1 & Norm 2 — Math_Score vector
- [x] 📌 Angle — between Math & Science score vectors

---

## ✅ Results Summary

| Analysis | Key Finding | Verdict |
|---|---|---|
| 📊 Mean / Median / Mode | Central tendency of Math scores | ✅ Distribution shape identified |
| 📏 Variance & Std Dev | Spread of Science scores | ✅ Score consistency measured |
| 🎲 P(Pass) | Baseline pass probability computed | ✅ Class pass rate established |
| 🔗 P(Pass \| Hours > 5) | Significantly higher than P(Pass) | ✅ Study hours strongly predict passing |
| 📈 Histogram + Curve | Math scores overlaid with normal curve | ✅ Distribution shape visualized |
| 〰️ Skewness & Kurtosis | Science scores show slight skewness | ✅ Most students score near average |
| 📉 Q-Q Plot | English scores tested for normality | ✅ Normality assumption verified |
| ✖️ Dot Product | Positive value between Math & Science | ✅ Positive performance correlation |
| 📐 Angle θ | Small angle between score vectors | ✅ Math & Science performance aligned |

---

## 🚀 How to Run

### 📋 Prerequisites

```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

### 🛠️ Step-by-Step

**Step 1 — Clone the repository**
```bash
git clone https://github.com/meet6949/stats-linear-algebra-exam.git
cd stats-linear-algebra-exam
```

**Step 2 — Place the dataset in the project folder**
```
stats-linear-algebra-exam/
└── students_scores.csv    ← put your CSV here
```

**Step 3 — Launch Jupyter Notebook**
```bash
jupyter notebook Final_Practica_Exam.ipynb
```

**Step 4 — Run All Cells**
```
Kernel → Restart & Run All
```
> Or press `Shift + Enter` to run cell by cell.

---

## 📁 File Structure

```
📦 Final_Practical_Exam/
│
├── 📓 Final_Practica_Exam.ipynb     ← Main Jupyter Notebook (Part B)
├── 📊 students_scores.csv           ← Student score dataset
│
├── 📈 Generated Plots
│   ├── plot_01_central_tendency.png
│   ├── plot_02_dispersion.png
│   ├── plot_03_probability.png
│   ├── plot_04_histogram_normal.png
│   ├── plot_05_skewness_kurtosis.png
│   ├── plot_06_qqplot.png
│   └── plot_07_vectors_angle.png
│
├── 📋 README.md                     ← This file (Theory + Overview)
└── 📋 THEORY_ANSWERS.md             ← Part A short-answer theory
```

---

## 🧠 Key Concepts Quick Reference

```
📌 Mean / Median / Mode     →  Central tendency; mean = Σx/n
📌 Range                    →  Max − Min; total span of values
📌 Variance (σ²)            →  Average squared deviation from mean
📌 Std Deviation (σ)        →  √Variance; same unit as original data
📌 P(A)                     →  Favourable / Total outcomes
📌 Conditional Probability  →  P(A|B) = P(A∩B) / P(B)
📌 Contingency Table        →  Cross-tabulation of two categorical variables
📌 Normal Distribution      →  Symmetric bell curve; defined by μ and σ
📌 Skewness                 →  Asymmetry of distribution (+ = right tail)
📌 Kurtosis                 →  Tail heaviness vs normal distribution
📌 Q-Q Plot                 →  Normality test — points on diagonal = normal fit
📌 Vector                   →  Array of scores representing a group of students
📌 Dot Product              →  Σ(aᵢ × bᵢ); measures directional similarity
📌 Norm 1 (L1)              →  Sum of absolute values: Σ|aᵢ|
📌 Norm 2 (L2)              →  Euclidean length: √(Σaᵢ²)
📌 Angle between vectors    →  cos⁻¹(A·B / ||A||·||B||); low angle = high similarity
```

---

## 📌 Assumptions

1. Significance level **α = 0.05** used throughout
2. Pass/Fail threshold defined by the dataset's `Pass_Fail` column directly
3. Conditional probability computed using raw contingency table counts
4. Vectors are constructed from the **first 5 students** in the dataset
5. Normal curve overlay uses sample mean and std dev of `Math_Score`

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" width="100%"/>

**Made with ❤️ by [Meet Gajera](https://github.com/meet6949)**

*Stats & Linear Algebra Exam — Where Every Formula Tells a Story*

⭐ *If this project helped you, consider giving it a star!* ⭐

</div>
