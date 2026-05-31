<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Derivable%20Judgement&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=35&desc=A%20Statistical%20Decision-Making%20Model%20on%20Public%20Health%20Data&descAlignY=55&descSize=18" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
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
- [🧠 Quick Reference](#-key-concepts-quick-reference)

</details>

---

## 🎯 Project Overview

<table>
<tr>
<td>

You are a **data analyst at a public health research organization**. Armed with 500 health records, your mission is to use the power of **inferential statistics** to uncover hidden patterns — and *derive real judgements* about what factors drive disease.

**The data covers:**
- 🧑‍🤝‍🧑 Demographics — gender, age groups, regions
- 🚬 Lifestyle habits — smoking, exercise
- 🩺 Diseases — Diabetes, Hypertension
- 📊 Clinical metrics — BMI, Blood Pressure, Glucose, Cholesterol

**The goal:** Move beyond raw numbers. Let statistics *speak*.

</td>
<td>

```
📦 500 Patient Records
        │
        ▼
🔍 Exploratory Analysis
        │
        ▼
📐 Hypothesis Testing
        │
        ▼
📈 Statistical Inference
        │
        ▼
✅ Derivable Judgements
```

</td>
</tr>
</table>

---

## 🗄️ Dataset Structure

> **File:** `health_dataset.csv` &nbsp;|&nbsp; **Records:** `500` &nbsp;|&nbsp; **Features:** `15`

| # | Field Name | Data Type | Description |
|---|------------|-----------|-------------|
| 1 | `record_id` | String | 🔑 Unique identifier for each health record |
| 2 | `age` | Int | 🎂 Actual age of individual |
| 3 | `age_group` | String | 📊 `"18-25"` · `"26-35"` · `"36-45"` · `"46-60"` · `"60+"` |
| 4 | `gender` | String | 👤 `"Male"` · `"Female"` · `"Other"` |
| 5 | `weight` | Int | ⚖️ Weight in kilograms |
| 6 | `region` | String | 🗺️ `"North"` · `"South"` · `"East"` · `"West"` |
| 7 | `smoking_status` | String | 🚬 `"Smoker"` · `"Non-Smoker"` · `"Former Smoker"` |
| 8 | `exercise_frequency` | String | 🏃 `"Daily"` · `"Weekly"` · `"Rarely"` · `"Never"` |
| 9 | `bmi` | Float | 📏 Body Mass Index = weight(kg) / height(m)² |
| 10 | `blood_pressure` | Float | 💉 Systolic blood pressure in mmHg |
| 11 | `diabetes` | Boolean | 🩸 Has diabetes? `True` / `False` |
| 12 | `hypertension` | Boolean | ❤️ Has hypertension? `True` / `False` |
| 13 | `cholesterol_level` | Float | 🧪 Total cholesterol in mg/dL |
| 14 | `glucose_level` | Float | 🍬 Fasting glucose level in mg/dL |
| 15 | `visit_date` | Date | 📅 Date of health check-up |

---

## 📚 Theoretical Foundation (Part A)

> 💡 **8 Core Concepts** that form the backbone of this project.

<details>
<summary><b>1️⃣ Inferential Statistics</b> — Drawing big conclusions from small data</summary>

<br/>

**Definition:** Inferential statistics allows us to draw conclusions about an entire **population** based on a **sample**.

```
Sample (500 records) ──→ Statistical Analysis ──→ Inference about Population
```

Studying every individual in a population is impractical. Instead, we take a representative sample and use probability theory to **generalize**.

> 📌 *In this project:* Our 500 records are used to make claims about **all** individuals in the region.

<br/>
</details>

<details>
<summary><b>2️⃣ Hypothesis Testing</b> — The court trial of statistics</summary>

<br/>

**Definition:** A formal, structured method to test a specific claim about a population using sample evidence — like a court trial where H₀ is "innocent until proven guilty."

| Component | Symbol | Meaning |
|-----------|--------|---------|
| **Null Hypothesis** | H₀ | Default: "nothing is happening" |
| **Alternative Hypothesis** | H₁ | Claim: "something IS happening" |
| **Significance Level** | α | Usually `0.05` (5% threshold) |
| **Test Statistic** | Z / T / F / χ² | Calculated from sample data |

**7-Step Process:**
```
1. State H₀ and H₁
2. Set significance level (α = 0.05)
3. Choose the right test (Z / T / Chi-Square / ANOVA)
4. Calculate test statistic from sample
5. Find p-value
6. Decision: Reject H₀ if p < α
7. State conclusion in plain English
```

<br/>
</details>

<details>
<summary><b>3️⃣ Confidence Intervals & Critical Values</b> — The range of truth</summary>

<br/>

**Confidence Interval:** A range that likely contains the true population parameter.

```
CI Formula:  x̄  ±  Z* × (σ / √n)

  x̄  = sample mean
  Z* = critical value (1.96 for 95% CI)
  σ  = standard deviation
  n  = sample size
```

> ⚠️ A 95% CI does **NOT** mean "95% chance the true value is in here." The true value is fixed — the *interval* is what changes each time you sample!

| Test | Two-tailed (α=0.05) | One-tailed (α=0.05) |
|------|---------------------|---------------------|
| Z-test | ±1.96 | ±1.645 |
| Chi-Square (df=1) | 3.841 | — |

<br/>
</details>

<details>
<summary><b>4️⃣ P-Value</b> — How rare is your result?</summary>

<br/>

**Definition:** The probability of observing results as extreme as yours, *assuming H₀ is true.*

```
p-value < 0.05  ──→  Reject H₀  ──→  ✅ Statistically Significant
p-value ≥ 0.05  ──→  Fail to Reject H₀  ──→  ❌ Insufficient Evidence
```

> 🎯 Think of it as: "How likely is this result if nothing was actually happening?" Small p = something real is going on.

> ⚠️ Small p-value ≠ Large effect. Significance is not the same as importance!

<br/>
</details>

<details>
<summary><b>5️⃣ Type I & Type II Errors</b> — The two ways you can be wrong</summary>

<br/>

| | H₀ is **TRUE** | H₀ is **FALSE** |
|---|---|---|
| **Reject H₀** | ❌ Type I Error (False Positive) | ✅ Correct! |
| **Don't Reject H₀** | ✅ Correct! | ❌ Type II Error (False Negative) |

| Error | Symbol | Real-World Analogy |
|-------|--------|--------------------|
| **Type I** | α | 🔔 Fire alarm rings — but no fire |
| **Type II** | β | 🔕 Fire exists — but alarm stays silent |

> 💡 Lowering α reduces Type I errors but increases Type II errors. Increasing sample size reduces **both**.

<br/>
</details>

<details>
<summary><b>6️⃣ Statistical Tests</b> — Choosing the right weapon</summary>

<br/>

| Test | When to Use | Formula |
|------|-------------|---------|
| **Z-Test** | Large sample (n > 30), σ known | `Z = (x̄ - μ₀) / (σ / √n)` |
| **T-Test** | Small sample (n < 30), σ unknown | `t = (x̄ - μ₀) / (s / √n)` |
| **Chi-Square** | Categorical variables, independence testing | `χ² = Σ [(O - E)² / E]` |
| **ANOVA** | Compare means of 3+ groups | `F = Between-group var / Within-group var` |

> 💡 **Why not just use multiple T-tests instead of ANOVA?** Multiple T-tests inflate Type I error. ANOVA controls for this by testing all groups simultaneously.

<br/>
</details>

<details>
<summary><b>7️⃣ Covariance</b> — Do variables move together?</summary>

<br/>

**Definition:** Measures the *direction* of the linear relationship between two numerical variables.

```
Cov(X, Y) = Σ[(xᵢ - x̄)(yᵢ - ȳ)] / (n - 1)

  Cov > 0  →  Both increase together  📈
  Cov < 0  →  One increases as other decreases  📉
  Cov = 0  →  No linear relationship  ➡️
```

> ⚠️ **Limitation:** Covariance depends on units. You can't compare it across different variable pairs. That's why we use Correlation.

<br/>
</details>

<details>
<summary><b>8️⃣ Correlation</b> — Strength + Direction, standardized</summary>

<br/>

**Definition:** Standardizes covariance into a unitless measure from **-1 to +1**.

```
r = Cov(X, Y) / (σₓ × σᵧ)
```

| r Value | Interpretation |
|---------|---------------|
| +0.9 to +1.0 | 🟢 Very strong positive |
| +0.7 to +0.9 | 🟢 Strong positive |
| +0.4 to +0.7 | 🟡 Moderate positive |
| +0.1 to +0.4 | 🟡 Weak positive |
| ~0 | ⚪ No linear relationship |
| -0.1 to -0.4 | 🟠 Weak negative |
| -0.4 to -0.7 | 🟠 Moderate negative |
| -0.7 to -1.0 | 🔴 Strong to very strong negative |

> ⚠️ **CORRELATION ≠ CAUSATION** — Ice cream sales and drownings are both correlated with summer heat, not with each other!

<br/>
</details>

---

## 🔬 Analysis Tasks (Part B)

### 🧪 Hypotheses Tested

| # | Null Hypothesis (H₀) | Alternative Hypothesis (H₁) | Test |
|---|----------------------|------------------------------|------|
| **H1** | Smoking has no effect on Diabetes | Smoking affects Diabetes prevalence | 🔲 Chi-Square |
| **H2** | Mean BMI is same across age groups | Mean BMI differs across age groups | 📊 One-Way ANOVA |
| **H3** | Exercise has no link to Hypertension | Exercise is associated with Hypertension | 🔲 Chi-Square |
| **H4** | Blood pressure equal: smokers vs non-smokers | Smokers have higher blood pressure | 📏 Z-Test / T-Test |

### ✔️ Tasks Completed

- [x] 🏗️ Dataset generation with 500 realistic health records
- [x] 📊 Descriptive statistics for all variables
- [x] 📐 95% Confidence Intervals for 6 numerical variables
- [x] 🔢 Critical value & p-value calculation
- [x] 📏 Z-test — Blood Pressure: Smokers vs Non-Smokers
- [x] 📏 T-test — Glucose Level: Diabetic vs Non-Diabetic
- [x] 🔲 Chi-Square — Smoking vs Diabetes
- [x] 🔲 Chi-Square — Exercise vs Hypertension
- [x] 📊 One-Way ANOVA — BMI across Age Groups
- [x] 🧮 Covariance Matrix for all numerical variables
- [x] 📈 Pearson Correlation Matrix with significance testing

---

## ✅ Results Summary

| Hypothesis | Test Used | Statistic | P-Value | Decision | Conclusion |
|-----------|-----------|-----------|---------|----------|------------|
| 🚬 Smoking → Diabetes | Chi-Square | ~6.8 | < 0.05 | ✅ Reject H₀ | Smoking significantly affects Diabetes |
| ⚖️ BMI across Age Groups | F (ANOVA) | ~3.2 | < 0.05 | ✅ Reject H₀ | BMI differs across age groups |
| 🏃 Exercise → Hypertension | Chi-Square | ~8.1 | < 0.05 | ✅ Reject H₀ | Exercise reduces Hypertension risk |
| 💉 BP: Smokers vs Non-Smokers | Z/T-Test | ~2.4 | < 0.05 | ✅ Reject H₀ | Smokers have higher blood pressure |

> 📝 *Exact values may vary slightly — run the notebook for precise results.*

---

## 🚀 How to Run

### 📋 Prerequisites

```bash
pip install pandas numpy scipy statsmodels faker jupyter
```

### 🛠️ Step-by-Step

**Step 1 — Generate the Dataset**
```bash
python generate_dataset.py
```
> Creates `health_dataset.csv` with 500 synthetic health records.

**Step 2 — Launch the Notebook**
```bash
jupyter notebook Derivable_Judgement_Statistics.ipynb
```

**Step 3 — Run All Cells**
```
Kernel → Restart & Run All
```
> Or press `Shift + Enter` to run cell by cell.

---

## 📁 File Structure

```
📦 derivable-judgement/
│
├── 📓 Derivable_Judgement_Statistics.ipynb   ← Main analysis notebook
├── 🐍 generate_dataset.py                    ← Synthetic dataset generator
├── 📊 health_dataset.csv                     ← 500 records × 15 features
├── 📄 PartA_Theory.md                        ← Theoretical foundation (all 8 concepts)
└── 📄 README.md                              ← This file
```

---

## 🧠 Key Concepts Quick Reference

```
📌 Inferential Statistics  →  Draw conclusions about population from sample
📌 Hypothesis Testing      →  Formal test of a claim using H₀ and H₁
📌 Confidence Interval     →  Range that likely contains true population value
📌 P-Value                 →  Probability of result if H₀ were true
📌 Type I Error (α)        →  False alarm — rejecting true H₀
📌 Type II Error (β)       →  Missed signal — not rejecting false H₀
📌 Z-Test                  →  Large sample mean comparison (n > 30)
📌 T-Test                  →  Small sample mean comparison (n < 30)
📌 Chi-Square              →  Categorical variable independence test
📌 ANOVA                   →  Mean comparison across 3+ groups
📌 Covariance              →  Direction of relationship (unit-dependent)
📌 Correlation (r)         →  Direction + strength of relationship (−1 to +1)
```

---

## 📌 Assumptions

1. Dataset is synthetically generated with realistic distributions
2. Significance level **α = 0.05** used throughout
3. Z-test applied when group n > 30; T-test otherwise
4. Pearson correlation used (assumes approximate normality for large n)
5. Independence of observations assumed

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

**Made with ❤️ by Meet Gajera**

*Derivable Judgement — Where Data Speaks*

⭐ *If this project helped you, consider giving it a star!* ⭐

</div>
