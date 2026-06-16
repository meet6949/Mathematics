<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=Stats%20%26%20Linear%20Algebra&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=35&desc=A%20Statistics%20%26%20Linear%20Algebra%20Practical%20Exam%20on%20Real%20Student%20Score%20Data&descAlignY=55&descSize=17" width="100%"/>

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

> *✨ "Data is the new oil — and Statistics is the refinery." ✨*

<br/>

**⏱️ Type:** Final Practical Exam &nbsp;&nbsp;**|**&nbsp;&nbsp; **🧪 Subject:** Statistics + Linear Algebra &nbsp;&nbsp;**|**&nbsp;&nbsp; **🎓 Domain:** Student Performance Analytics

**👨‍💻 Author:** [Meet Gajera](https://github.com/meet6949)

<br/>

</div>

---

## 📌 Table of Contents

<details open>
<summary><b>Click to expand / collapse</b></summary>

- [🎯 Project Overview](#-project-overview)
- [🗄️ Dataset Structure](#️-dataset-structure)
- [📚 Theoretical Foundation](#-theoretical-foundation-part-a)
- [🔬 Practical Implementation](#-practical-implementation-part-b)
- [📊 Visualizations & Insights](#-visualizations--insights)
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

You are a **data analyst examining real student exam records**. Armed with subject-wise scores across Math, Science, and English — along with study hours and pass/fail labels — your mission is to apply **statistics and linear algebra** to uncover what drives student performance.

**The data covers:**
- 📐 Math, Science & English exam scores per student
- ⏱️ Hours studied per student
- ✅ Pass / Fail classification (1 = Pass, 0 = Fail)

**The goal:** Compute central tendency, analyze probability, visualize distributions, and apply vector algebra to draw *data-driven insights* about academic performance.

</td>
<td>

```
📦 Student Score Records
         │
         ▼
📊 Central Tendency & Dispersion
         │
         ▼
🎲 Probability & Contingency
         │
         ▼
📈 Distribution & Visualization
         │
         ▼
🔢 Linear Algebra (Vectors)
         │
         ▼
✅ Insights & Conclusions
```

</td>
</tr>
</table>

---

## 🗄️ Dataset Structure

> **File:** `students_scores.csv` &nbsp;|&nbsp; **Features:** `5` &nbsp;|&nbsp; **Type:** Real student exam records

| # | Field Name | Data Type | Description |
|---|------------|-----------|-------------|
| 1 | `Math_Score` | Float | 📐 Student's mathematics exam score (0–100) |
| 2 | `Science_Score` | Float | 🔬 Student's science exam score (0–100) |
| 3 | `English_Score` | Float | 📖 Student's English exam score (0–100) |
| 4 | `Hours_Studied` | Float | ⏱️ Total hours the student studied |
| 5 | `Pass_Fail` | Int | ✅ `1` = Pass · `0` = Fail |

---

## 📚 Theoretical Foundation (Part A)

> 💡 **6 Core Concepts** — formulas, intuition, and how each is applied in this project.

<details>
<summary><b>1️⃣ Measures of Central Tendency</b> — Where does the data center?</summary>

<br/>

**Definition:** Central tendency describes the most representative single value of a dataset.

```
Mean   (μ) = Σx / n              → Arithmetic average
Median     = Middle value         → Robust to outliers
Mode       = Most frequent value  → Tells us the "peak"
```

**When to use which:**
| Measure | Best Used When | Affected by Outliers? |
|---|---|---|
| Mean | Symmetric, no extreme values | ✅ Yes |
| Median | Skewed data or outliers present | ❌ No |
| Mode | Categorical or discrete data | ❌ No |

> 📌 *In this project:* Applied to `Math_Score`.
> Mean ≈ **75.42** → most students score around 75.
> Mode = **100** → a significant chunk of students scored full marks.

<br/>
</details>

<details>
<summary><b>2️⃣ Measures of Dispersion</b> — How spread out is the data?</summary>

<br/>

**Definition:** Dispersion tells us how much the values vary from the center.

```
Range    = Max − Min
Variance = Σ(xᵢ − μ)² / n       → Avg squared deviation
Std Dev  = √Variance              → Same unit as data
```

**Rule of thumb:**
- **Low σ** → students are consistent (scores cluster near mean)
- **High σ** → wide variation (some very high, some very low)

> 📌 *In this project:* Applied to `Science_Score` — reveals how consistently (or inconsistently) students performed in Science.

<br/>
</details>

<details>
<summary><b>3️⃣ Probability & Conditional Probability</b> — What are the chances?</summary>

<br/>

**Basic Probability:**
```
P(A) = Favourable outcomes / Total outcomes
```

**Conditional Probability:**
```
P(A | B) = P(A ∩ B) / P(B)

→ "Probability of A, given B has already occurred"
```

**Contingency Table approach:**
```
                Hours > 5     Hours ≤ 5
  Pass     |      a         |     b      |
  Fail     |      c         |     d      |

P(Pass | Hours > 5) = a / (a + c)
```

> 📌 *In this project:*
> - Computed **P(Pass)** as overall class pass rate
> - Built contingency table: `Pass_Fail` vs `Hours_Studied > 5`
> - Computed **P(Pass | Hours_Studied > 5)** — and found it to be significantly higher → **study hours strongly predict passing**

<br/>
</details>

<details>
<summary><b>4️⃣ Normal Distribution & Histogram</b> — The bell curve</summary>

<br/>

A symmetric, bell-shaped distribution defined by mean μ and std dev σ.

```
PDF: f(x) = [1/(σ√2π)] × exp[−(x − μ)² / (2σ²)]

Empirical Rule:
  68.3%  of data lies within  μ ± 1σ
  95.4%  of data lies within  μ ± 2σ
  99.7%  of data lies within  μ ± 3σ
```

A **KDE (Kernel Density Estimate)** curve smooths the histogram to show the underlying probability shape.

> 📌 *In this project:* `sns.histplot(df['Math_Score'], kde=True)` → Histogram with KDE overlay on Math Scores.

<br/>
</details>

<details>
<summary><b>5️⃣ Skewness & Kurtosis</b> — Shape of the distribution</summary>

<br/>

```
Skewness = Σ((xᵢ − μ) / σ)³ / n

  > 0  →  Right-skewed  (long right tail — few very high scorers)
  < 0  →  Left-skewed   (long left tail — few very low scorers)
  = 0  →  Symmetric     (perfect bell curve)

Kurtosis = Σ((xᵢ − μ) / σ)⁴ / n − 3

  > 0  →  Leptokurtic   (sharp peak, heavy tails)
  < 0  →  Platykurtic   (flat peak, light tails)
  = 0  →  Mesokurtic    (normal distribution)
```

> 📌 *In this project:* Applied to `Science_Score` — measures whether scores are symmetric or skewed, and whether they have a sharp or flat distribution.

<br/>
</details>

<details>
<summary><b>6️⃣ Q-Q Plot</b> — Normality testing without histograms</summary>

<br/>

**Definition:** A Quantile-Quantile plot compares the quantiles of your data against a theoretical normal distribution.

**How to read it:**
- Points on the **45° red line** → data is normally distributed ✓
- **Curved tails** → skewness or heavy tails in data
- **S-shaped curve** → kurtosis mismatch

> 📌 *In this project:* Q-Q Plot of `English_Score` — central values follow the diagonal closely (near-normal), but both tails deviate slightly due to the natural ceiling of exam scores at 100. **Conclusion: English Scores are approximately normal in the central range.**

<br/>
</details>

<details>
<summary><b>7️⃣ Linear Algebra — Vectors, Dot Product & Norms</b> — Geometry of scores</summary>

<br/>

**Represent student scores as mathematical vectors:**

```
Math_Vector    = [s₁, s₂, s₃, s₄, s₅]   ← first 5 students' Math scores
Science_Vector = [s₁, s₂, s₃, s₄, s₅]   ← first 5 students' Science scores
```

**Core operations:**
```
Dot Product:   A · B = Σ(aᵢ × bᵢ)
                → Measures directional similarity between vectors
                → Positive = same direction = positive correlation

Norm 1 (L1):  ||A||₁ = Σ|aᵢ|
               → Manhattan distance / total absolute magnitude

Norm 2 (L2):  ||A||₂ = √(Σaᵢ²)
               → Euclidean length — most natural measure of size

Angle:  θ = cos⁻¹( A·B / (||A||₂ × ||B||₂) )
         → Small θ  → vectors point in same direction → high similarity
         → θ = 0°   → perfectly aligned
         → θ = 90°  → completely independent
```

> 📌 *In this project:* A **positive dot product** and **small angle** between Math and Science vectors confirm that students who score well in Math also tend to score well in Science — a strong cross-subject correlation.

<br/>
</details>

---

## 🔬 Practical Implementation (Part B)

### 📋 All Tasks Completed

**Step 1 — Central Tendency & Dispersion**
- [x] 📊 `df['Math_Score'].mean()` → Mean of Math Score
- [x] 📊 `df['Math_Score'].median()` → Median of Math Score
- [x] 📊 `df['Math_Score'].mode()` → Mode of Math Score
- [x] 📏 `max - min` → Range of Science Score
- [x] 📏 `df['Science_Score'].var()` → Variance of Science Score
- [x] 📏 `df['Science_Score'].std()` → Standard Deviation of Science Score

**Step 2 — Probability**
- [x] 🎲 `(df['Pass_Fail'] == 1).mean()` → P(Pass) overall
- [x] 📋 `pd.crosstab(Pass_Fail, Hours_Studied > 5)` → Contingency Table
- [x] 🔗 Boolean masking → P(Pass | Hours_Studied > 5)

**Step 3 — Distribution & Visualization**
- [x] 📈 `sns.histplot(..., kde=True)` → Histogram + KDE for Math_Score
- [x] 〰️ `.skew()` & `.kurt()` → Skewness & Kurtosis of Science_Score
- [x] 📉 `stats.probplot(...)` → Q-Q Plot for English_Score

**Step 4 — Linear Algebra**
- [x] 🔢 `.head(5).values` → Math & Science vectors (first 5 students)
- [x] ✖️ `np.dot(math_vector, science_vector)` → Dot Product
- [x] 📐 `np.linalg.norm(..., ord=1)` → Norm 1 of Math vector
- [x] 📐 `np.linalg.norm(..., ord=2)` → Norm 2 of Math vector
- [x] 📌 `np.degrees(np.arccos(cos_theta))` → Angle between vectors

---

## 📊 Visualizations & Insights

### 📈 Plot 1 — Histogram + KDE Curve (Math Score)

> Generated with: `sns.histplot(df['Math_Score'], kde=True)`

**What it shows:**
- The distribution of Math Scores across all students with a smoothed KDE curve
- Scores are **slightly left-skewed** (skewness ≈ −0.28) — most students scored on the **higher side**
- Strong concentration of scores between **60–100**
- Peak around **75–80**, aligning with the mean of **75.42**
- Mode = **100** → a significant number of students scored full marks
- Distribution is **platykurtic** (kurtosis ≈ −0.51) — flatter than a normal curve, scores are more spread out

```
Interpretation: High-performing class overall, with no extreme low scorers.
Most students fall in the 60–100 range. The flat distribution means performance
is more evenly spread rather than sharply peaked at one score.
```

---

### 📉 Plot 2 — Q-Q Plot (English Score)

> Generated with: `stats.probplot(df['English_Score'], dist='norm', plot=plt)`

**What it shows:**
- Each point = a quantile of English Score plotted against the expected normal quantile
- The **middle portion** closely follows the red diagonal line → near-normal in the central range
- **Lower tail** dips below the line → slight deficit of very low scores
- **Upper tail** flattens → natural ceiling effect at score = 100

```
Interpretation: English Scores are approximately normally distributed
in the central range. Tail deviations are expected for exam scores
since scores are bounded [0, 100].
```

---

### 🔢 Linear Algebra Summary (Vectors)

> Vectors built from first 5 students' Math & Science scores

```
Math Vector    = df['Math_Score'].head(5).values
Science Vector = df['Science_Score'].head(5).values

Dot Product    → np.dot(math_vector, science_vector)
Norm 1 (L1)   → np.linalg.norm(math_vector, ord=1)
Norm 2 (L2)   → np.linalg.norm(math_vector, ord=2)
Angle (θ°)    → np.degrees(np.arccos(cos_theta))
```

**Geometric interpretation:**
- A **large positive dot product** = both vectors point roughly in the same direction
- A **small angle** (close to 0°) = students who do well in Math also do well in Science
- **Norm 2** = the Euclidean "length" of the score vector in 5-dimensional space

---

## ✅ Results Summary

| # | Analysis | Method Used | Key Finding |
|---|---|---|---|
| 1 | 📊 Mean of Math Score | `.mean()` | ≈ **75.42** — class average performance |
| 2 | 📊 Mode of Math Score | `.mode()` | **100** — highest count at full marks |
| 3 | 📏 Std Dev of Science | `.std()` | Reveals score spread consistency |
| 4 | 🎲 P(Pass) | `.mean()` on Pass_Fail | Baseline class pass rate computed |
| 5 | 🔗 P(Pass \| Hours > 5) | Boolean mask + crosstab | Significantly higher than P(Pass) ✅ |
| 6 | 📈 Histogram + KDE | `sns.histplot(kde=True)` | Left-skewed, platykurtic, peak at 75–80 |
| 7 | 〰️ Skewness | `.skew()` | Math ≈ −0.28 → slight left skew |
| 8 | 〰️ Kurtosis | `.kurt()` | ≈ −0.51 → platykurtic (flat) |
| 9 | 📉 Q-Q Plot | `stats.probplot()` | English scores ≈ normal in central range |
| 10 | ✖️ Dot Product | `np.dot()` | Positive → Math & Science performance aligned |
| 11 | 📐 Angle θ | `np.arccos()` | Small angle → strong cross-subject correlation |

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
> Or press `Shift + Enter` to run cell by cell. Plots appear inline inside the notebook.

---

## 📁 File Structure

```
📦 Final_Practical_Exam/
│
├── 📓 Final_Practica_Exam.ipynb     ← Main Jupyter Notebook (all 4 steps)
├── 📊 students_scores.csv           ← Student score dataset (5 features)
│
├── 📈 Generated Plots (inline in notebook)
│   ├── Histogram + KDE — Math Score
│   └── Q-Q Plot — English Score
│
├── 📋 README.md                     ← This file
└── 📋 THEORY_ANSWERS.md             ← Part A short-answer theory
```

---

## 🧠 Key Concepts Quick Reference

```
📌 Mean / Median / Mode      →  Central tendency; mean = Σx/n
📌 Range                     →  Max − Min; total span of values
📌 Variance (σ²)             →  Avg squared deviation from mean
📌 Std Deviation (σ)         →  √Variance; same unit as data
📌 Skewness                  →  < 0 = left tail; > 0 = right tail; 0 = symmetric
📌 Kurtosis                  →  < 0 = flat (platykurtic); > 0 = sharp (leptokurtic)
📌 P(A)                      →  Favourable outcomes / Total outcomes
📌 Conditional P(A|B)        →  P(A∩B) / P(B) — probability given a condition
📌 Contingency Table         →  Cross-tabulation of two categorical variables
📌 Histogram + KDE           →  Visual distribution shape with smoothed curve
📌 Q-Q Plot                  →  Normality test — points on diagonal = normally distributed
📌 Vector                    →  Array of n scores in n-dimensional space
📌 Dot Product (A·B)         →  Σ(aᵢ×bᵢ) — directional similarity; positive = correlated
📌 Norm 1 (L1)               →  Manhattan: Σ|aᵢ|
📌 Norm 2 (L2)               →  Euclidean: √(Σaᵢ²) — standard vector length
📌 Angle θ                   →  cos⁻¹(A·B / ||A||·||B||) — 0° = identical; 90° = independent
```

---

## 📌 Assumptions

1. Significance level **α = 0.05** used throughout for all statistical interpretations
2. `Pass_Fail` column used directly — no custom threshold applied
3. Conditional probability computed via raw boolean masking on the DataFrame
4. Vectors are constructed from the **first 5 students** (rows 0–4) of the dataset
5. KDE curve in histogram uses default bandwidth estimation from seaborn
6. Q-Q Plot compared against the **standard normal distribution** via `scipy.stats.probplot`

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" width="100%"/>

**Made with ❤️ by [Meet Gajera](https://github.com/meet6949)**

*Stats & Linear Algebra Exam — Where Every Formula Tells a Story*

⭐ *If this project helped you, consider giving it a star!* ⭐

</div>
