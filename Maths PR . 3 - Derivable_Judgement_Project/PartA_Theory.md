<div align="center">

# 📚 Part A: Theoretical Foundation
### Derivable Judgement — Statistical Decision-Making Model

**👨‍💻 Student:** Meet Gajera &nbsp;&nbsp;|&nbsp;&nbsp; **📁 Project:** Derivable Judgement

</div>

---

> 💡 **8 core statistical concepts** that form the backbone of this project — explained clearly with examples, formulas, and visual cues.

---

## 📋 Index

| # | Concept | One-liner |
|---|---------|-----------|
| [1](#1️⃣-inferential-statistics) | Inferential Statistics | Conclude about populations from samples |
| [2](#2️⃣-hypothesis-testing) | Hypothesis Testing | Prove/disprove a statistical claim |
| [3](#3️⃣-confidence-intervals) | Confidence Intervals | Range likely containing the true value |
| [4](#4️⃣-correlation-vs-causation) | Correlation vs Causation | Related ≠ Responsible |
| [5](#5️⃣-type-i-and-type-ii-errors) | Type I & II Errors | Two ways to be wrong |
| [6](#6️⃣-p-value) | P-Value | How rare is your result? |
| [7](#7️⃣-central-limit-theorem) | Central Limit Theorem | Why normal distribution is everywhere |
| [8](#8️⃣-statistical-tests-bonus) | Statistical Tests | Choosing the right test |

---

## 1️⃣ Inferential Statistics

> *"Making big conclusions from small data — responsibly."*

**📖 Definition:**
Inferential statistics is the branch of statistics that deals with making conclusions about a larger **population** based on a smaller **sample** of data.

**🤔 Why do we use it?**
It is impossible to study every single person in a population. So, we take a small representative sample, study it, and use mathematics to *infer* the behavior of the whole group.

```
          Population
         (All patients)
              │
              │  Random Sampling
              ▼
         Sample Data
        (500 records)
              │
              │  Inferential Statistics
              ▼
         Conclusions about
         the full Population
```

> 📌 **In this project:** Our 500 health records are used to make claims about *all individuals in the region*, not just the 500 we have.

---

## 2️⃣ Hypothesis Testing

> *"Like a court trial — innocent (H₀) until proven guilty beyond reasonable doubt."*

**📖 Definition:**
A formal, structured method to check if a claim about data is statistically supported using sample evidence.

### 🔑 Key Components

| Component | Symbol | What It Means |
|-----------|--------|---------------|
| **Null Hypothesis** | H₀ | Default assumption — "Nothing is happening" / "No relationship" |
| **Alternative Hypothesis** | H₁ (or Hₐ) | The claim we want to prove — "Something IS happening" |
| **Significance Level** | α | Usually `0.05` — our tolerance for being wrong |
| **Test Statistic** | Z / T / F / χ² | A number calculated from sample data to test H₀ |

### 🪜 The 7-Step Process

```
Step 1 → State H₀ and H₁ clearly
Step 2 → Set significance level (α = 0.05)
Step 3 → Choose the right test (Z / T / Chi-Square / ANOVA)
Step 4 → Calculate test statistic from sample
Step 5 → Find the p-value
Step 6 → Decision: Reject H₀ if p-value < α
Step 7 → Conclude in plain language
```

> 📌 **Example in project:**
> - **H₀:** Smoking has no effect on Diabetes
> - **H₁:** Smoking affects Diabetes prevalence
> - **Result:** p < 0.05 → Reject H₀ ✅

---

## 3️⃣ Confidence Intervals

> *"We don't know the exact truth — but we can be 95% sure it's in this range."*

**📖 Definition:**
A Confidence Interval (CI) is a range of values, derived from sample data, that is likely to contain the true value of an unknown **population parameter**.

### 📐 Formula

```
CI = x̄  ±  Z* × (σ / √n)

Where:
  x̄   = sample mean
  Z*  = critical value (1.96 for 95% CI)
  σ   = standard deviation
  n   = sample size
```

### 🧪 Example

If the average age of patients is **45 ± 5 with 95% confidence:**

```
We are 95% sure that the TRUE average age
of the entire population is between:

        40  ◄──────────────────►  50
             └──── 95% CI ────┘
```

> ⚠️ **Common Misconception:** A 95% CI does NOT mean "95% probability the true value is inside."
> The true value is fixed — the *interval* is what changes every time you re-sample.
> If you repeated sampling 100 times → 95 of those intervals would capture the true mean.

---

## 4️⃣ Correlation vs Causation

> *"Two things happening together doesn't mean one caused the other."*

### 📈 Correlation

Measures how strongly two variables **move together**, and in which direction.

```
Ice cream sales  📈   ──┐
                         ├── Both increase in summer ☀️
Drowning incidents 📈  ──┘

They are CORRELATED — but ice cream doesn't cause drowning!
```

### 💥 Causation

One variable **directly causes** a change in another.

```
Hand in fire 🔥  →  Burns your skin 🤕
        ↑
        TRUE Causation
```

### ⚠️ The Golden Rule

```
╔══════════════════════════════════════════════╗
║  CORRELATION  ≠  CAUSATION                  ║
║                                              ║
║  Just because two things happen together     ║
║  does NOT mean one caused the other.         ║
╚══════════════════════════════════════════════╝
```

> 📌 **Why it matters:** In health data, BMI and glucose may correlate — but correlation alone can't tell us which variable (if any) drives the other.

---

## 5️⃣ Type I and Type II Errors

> *"There are exactly two ways to be wrong — and they pull in opposite directions."*

**📖 Definition:**
Mistakes that can occur when making a decision in hypothesis testing.

### 📊 Error Table

| | H₀ is Actually **TRUE** | H₀ is Actually **FALSE** |
|---|---|---|
| **You Reject H₀** | ❌ **Type I Error** | ✅ Correct Decision |
| **You Fail to Reject H₀** | ✅ Correct Decision | ❌ **Type II Error** |

### 🔍 Detailed Breakdown

| Error Type | Also Known As | Symbol | Medical Analogy |
|------------|---------------|--------|-----------------|
| **Type I Error** | False Positive | α (alpha) | 🔔 Telling a **healthy** person they are sick |
| **Type II Error** | False Negative | β (beta) | 🔕 Telling a **sick** person they are healthy |

### ⚖️ The Tradeoff

```
Decrease α  →  Fewer Type I Errors  →  BUT more Type II Errors
Increase n  →  Reduces BOTH errors simultaneously ✅
```

> 💡 In medicine, **Type II errors** are often more dangerous (missing a real disease). In legal settings, **Type I errors** are worse (convicting an innocent person).

---

## 6️⃣ P-Value

> *"The smaller the p-value, the harder it is to explain your result as random luck."*

**📖 Definition:**
The p-value is the probability of obtaining results **as extreme as (or more extreme than)** the observed results, *assuming the Null Hypothesis (H₀) is true*.

### 🎯 Decision Rule

```
p-value < 0.05  ──→  Result is RARE if H₀ were true
                ──→  REJECT H₀
                ──→  ✅ Statistically Significant

p-value ≥ 0.05  ──→  Result could happen by chance
                ──→  FAIL TO REJECT H₀
                ──→  ❌ Insufficient Evidence
```

### 💡 Analogy

Think of the p-value as asking:
> *"If there was truly nothing going on, how often would I get a result this extreme just by luck?"*

- **Small p** = This would rarely happen by luck = Something real is happening ✅
- **Large p** = This could easily happen by luck = Maybe nothing is going on ❌

> ⚠️ **Important:** A small p-value does NOT mean the effect is large or practically important — it only means it's *statistically significant*.

---

## 7️⃣ Central Limit Theorem

> *"The most powerful idea in all of statistics."*

**📖 Definition:**
The Central Limit Theorem (CLT) states that if you take sufficiently large random samples from **any** population (regardless of its original distribution shape), the distribution of the **sample means** will approximate a **Normal Distribution** (Bell Curve).

```
Original Population                 Distribution of Sample Means
  (Any shape)                           (Always Normal!)

  ██                                        ▄▄
  ██  ██                                  ▄████▄
  ██  ██  ██           ─────────►       ▄████████▄
  ██  ██  ██  ██                      ▄████████████▄
──────────────────                  ─────────────────────
Skewed / Bimodal / Any            Beautiful Bell Curve ✅
```

### ❓ Why is CLT so important?

| Without CLT | With CLT |
|-------------|----------|
| Need to know population's exact distribution | Works with ANY distribution |
| Can't apply standard formulas | Can use normal probability formulas |
| Predictions are unreliable | Predictions become reliable |

```
Simple summary:
  More samples  →  Better Normal Curve  →  Easier, Reliable Calculations
```

> 📌 **In this project:** CLT is what allows us to use Z-tests and T-tests on health data without needing to know the exact distribution of blood pressure, glucose, etc.

---

## 8️⃣ Statistical Tests (Bonus)

> *"Choosing the right test is half the battle."*

| Test | Use When | Formula | Example in Project |
|------|----------|---------|-------------------|
| **Z-Test** | n > 30, σ known | `Z = (x̄ - μ₀) / (σ / √n)` | BP: Smokers vs Non-Smokers |
| **T-Test** | n < 30, σ unknown | `t = (x̄ - μ₀) / (s / √n)` | Glucose: Diabetic vs Non-Diabetic |
| **Chi-Square** | Categorical variables | `χ² = Σ [(O-E)² / E]` | Smoking vs Diabetes |
| **ANOVA** | 3+ group means | `F = Between / Within variance` | BMI across Age Groups |

### 🧭 Quick Decision Guide

```
What type of data?
├── Numerical
│   ├── 2 groups   →  Z-Test (n>30) or T-Test (n<30)
│   └── 3+ groups  →  ANOVA
└── Categorical
    └── Independence between two variables  →  Chi-Square Test
```

---

<div align="center">

---

**📝 Notes compiled by: Meet Gajera**

*Part of the **Derivable Judgement** project — Where Data Speaks*

</div>
