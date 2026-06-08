<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=Spread%20Locator&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=35&desc=A%20Statistical%20Distribution%20Analysis%20Model%20on%20E-Commerce%20Transactions&descAlignY=55&descSize=17" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-4CB391?style=for-the-badge)](https://seaborn.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-22c55e?style=for-the-badge)]()

<br/>

> *✨ "In God we trust. All others must bring data." — W. Edwards Deming ✨*

<br/>

**⏱️ Duration:** 6 Hours &nbsp;&nbsp;**|**&nbsp;&nbsp; **🧪 Type:** Theory + Practical &nbsp;&nbsp;**|**&nbsp;&nbsp; **🛒 Domain:** E-Commerce Analytics

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

You are a **data analyst at an e-commerce platform**. Armed with 220 real transaction records from January 2023, your mission is to use the power of **statistical distributions** to understand customer purchase behaviour — and *locate the spread* behind every rupee transacted.

**The data covers:**
- 🆔 Transaction & Customer IDs
- 💰 Transaction amounts (₹)
- 📅 Transaction dates (Jan 2023)
- 🗺️ Region — North, South, East, West
- ✅ Transaction status — Success / Fail
- 🔢 Weekly transaction count per customer

**The goal:** Fit the right distributions, test them, and derive *probability-based business decisions*.

</td>
<td>

```
📦 220 Transaction Records
         │
         ▼
🔍 Exploratory Analysis
         │
         ▼
📐 Distribution Fitting
         │
         ▼
📈 Statistical Inference
         │
         ▼
✅ Business Insights
```

</td>
</tr>
</table>

---

## 🗄️ Dataset Structure

> **File:** `spread_locator_dataset.csv` &nbsp;|&nbsp; **Records:** `220` &nbsp;|&nbsp; **Features:** `7`

| # | Field Name | Data Type | Description |
|---|------------|-----------|-------------|
| 1 | `transaction_id` | UUID/String | 🔑 Unique identifier for each transaction |
| 2 | `customer_id` | UUID/String | 👤 Unique identifier for each customer |
| 3 | `transaction_amount` | Float | 💰 Total transaction amount in ₹ |
| 4 | `transaction_date` | Date | 📅 Date of the transaction (Jan 2023) |
| 5 | `transaction_count` | Int | 🔢 Number of transactions by customer in that week |
| 6 | `region` | String | 🗺️ `"North"` · `"South"` · `"East"` · `"West"` |
| 7 | `transaction_status` | String | ✅ `"Success"` · `"Fail"` |

---

## 📚 Theoretical Foundation (Part A)

> 💡 **11 Core Concepts** — detailed notes with formulas, properties, and project-specific applications.

<details>
<summary><b>1️⃣ Statistical Distributions</b> — The backbone of all analysis</summary>

<br/>

**Definition:** A statistical distribution describes all possible values a random variable can take and how likely each value (or range) is to occur.

```
Raw Data ──→ Pattern of Values ──→ Statistical Distribution
```

**Key Parameters:**
| Parameter | Meaning |
|---|---|
| Mean (μ) | Central tendency / expected value |
| Variance (σ²) | Spread around the mean |
| Skewness | Asymmetry (right-skewed = long right tail) |
| Kurtosis | Tail heaviness |

> 📌 *In this project:* Knowing the distribution of `transaction_amount` lets us answer: *"What % of orders exceed ₹5000?"*

<br/>
</details>

<details>
<summary><b>2️⃣ Q-Q Plot</b> — Normality testing without histograms</summary>

<br/>

**Definition:** A Quantile-Quantile plot compares two probability distributions by plotting their quantiles against each other.

**How to read it:**
- Points on the **45° diagonal line** → data follows that distribution ✓
- **Curved/bent tails** → skewness or heavy tails
- **S-shaped curve** → kurtosis mismatch

> 📌 *In this project:* Raw amounts bend upward at the right tail. After log transformation, the Q-Q plot is nearly linear → **Log-Normal confirmed**.

<br/>
</details>

<details>
<summary><b>3️⃣ Discrete vs Continuous Distributions</b></summary>

<br/>

| Feature | Discrete | Continuous |
|---|---|---|
| Values | Countable (0, 1, 2, ...) | Uncountable (any real number) |
| Probability Tool | PMF | PDF |
| P(X = exact k) | Defined (can be > 0) | Always = 0 |
| Example | Daily order count | Order amount (₹) |
| Distributions | Bernoulli, Binomial, Poisson | Normal, Log-Normal, Gamma |

> 📌 *In this project:* `transaction_count` → Discrete &nbsp;|&nbsp; `transaction_amount` → Continuous &nbsp;|&nbsp; `transaction_status` → Binary/Discrete

<br/>
</details>

<details>
<summary><b>4️⃣ Bernoulli Distribution</b> — The simplest building block</summary>

<br/>

Models a single trial with two outcomes — Success (1) or Failure (0).

```
P(X = 1) = p          (success)
P(X = 0) = 1 − p      (failure)

Mean     = p
Variance = p(1 − p)
```

> 📌 *In this project:* Each transaction is a Bernoulli trial. **p ≈ 0.427** (42.7% of transactions succeed).

<br/>
</details>

<details>
<summary><b>5️⃣ Binomial Distribution</b> — n Bernoulli trials summed</summary>

<br/>

Models the number of successes in **n** independent Bernoulli trials.

```
P(X = k) = C(n,k) × p^k × (1−p)^(n−k)

Mean     = np
Variance = np(1−p)
```

> 📌 *In this project:* Weekly transaction count fits Binomial — each of a customer's weekly transactions has probability **p** of success.

> 💡 When n → ∞ and p → 0 such that np = λ, Binomial → Poisson (Poisson Limit Theorem)

<br/>
</details>

<details>
<summary><b>6️⃣ Log-Normal Distribution</b> — The distribution of money</summary>

<br/>

X follows Log-Normal if **ln(X) ~ Normal(μ, σ²)**.

```
PDF: f(x) = [1/(xσ√2π)] × exp[−(ln x − μ)² / (2σ²)]    for x > 0

Mean  = exp(μ + σ²/2)
Mode  = exp(μ − σ²)
```

**Key Properties:**
- Always positive — ideal for prices, incomes, amounts
- Right-skewed with a long tail
- Product of many independent factors → Log-Normal (Multiplicative CLT)

> 📌 *In this project:* `transaction_amount` is best described by Log-Normal — confirmed by Q-Q plot and KS test.

<br/>
</details>

<details>
<summary><b>7️⃣ Power Law Distribution</b> — The Pareto principle in data</summary>

<br/>

```
P(X > x) ∝ x^(−α)       (Survival / CCDF)
f(x)     ∝ x^(−α−1)     (PDF)
```

**Detection:** log(P(X > x)) vs log(x) gives a straight line with slope **−α**.

**Famous as:** Pareto 80-20 Rule — top 20% customers generate 80% revenue.

> 📌 *In this project:* Power Law fit reveals **α ≈ 2.5** — small fraction of high-value orders drive most revenue.

<br/>
</details>

<details>
<summary><b>8️⃣ Box-Cox Transformation</b> — Making data behave normally</summary>

<br/>

```
y(λ) = (x^λ − 1) / λ     if λ ≠ 0
y(λ) = ln(x)              if λ = 0
```

| λ Value | Transformation Applied |
|---|---|
| 1 | No change |
| 0 | Natural log |
| 0.5 | Square root |
| −1 | Reciprocal |

> ⚠️ Data must be strictly **positive (x > 0)** before applying Box-Cox.

> 📌 *In this project:* Optimal **λ ≈ 0.15** — near log-transform. Reduces skewness significantly.

<br/>
</details>

<details>
<summary><b>9️⃣ Poisson Distribution</b> — Counting independent events over time</summary>

<br/>

Models number of events in a fixed interval when events occur independently at constant rate λ.

```
P(X = k) = (e^(−λ) × λ^k) / k!

Mean = Variance = λ        ← unique property of Poisson!
```

**Example:** Hospital receives λ = 4 calls/hour.
P(exactly 7 calls) = (e⁻⁴ × 4⁷) / 7! ≈ 0.0595

> 📌 *In this project:* Daily transaction count follows **Poisson(λ ≈ 7.1)** — transactions arrive independently throughout January.

<br/>
</details>

<details>
<summary><b>🔟 Z-Score Probability</b> — Standardising for comparison</summary>

<br/>

```
Z = (X − μ) / σ

Z = 0   → value equals the mean
Z = 1   → 1 std dev above mean
|Z| > 3 → outlier (less than 0.3% of normal data)
```

**Empirical Rule:**
```
P(|Z| < 1) ≈ 68.3%
P(|Z| < 2) ≈ 95.4%
P(|Z| < 3) ≈ 99.7%
```

**For threshold probability:**
`P(X > threshold) = 1 − Φ(z)` where Φ is the standard normal CDF

> 📌 *In this project:* Used to compute **P(amount > ₹5000)** and flag outlier transactions.

<br/>
</details>

<details>
<summary><b>1️⃣1️⃣ PDF vs CDF</b> — Two sides of the same distribution</summary>

<br/>

| Feature | PDF | CDF |
|---|---|---|
| Full Name | Probability Density Function | Cumulative Distribution Function |
| Answers | "How dense is probability near x?" | "What is P(X ≤ x)?" |
| Range of output | 0 to +∞ | 0 to 1 |
| Shape | Varies (bell, skewed...) | Always S-shaped, monotone increasing |
| P(a < X < b) | Area under curve from a to b | F(b) − F(a) |

```
CDF(x) = ∫ PDF(t) dt        PDF(x) = d/dx CDF(x)
```

> 📌 *In this project:*
> **PDF** → Most amounts cluster between ₹1,000–₹4,000
> **CDF** → "What % of transactions fall below ₹3,000?" → Read F(3000)

<br/>
</details>

---

## 🔬 Analysis Tasks (Part B)

### 📋 Tasks Completed

- [x] 📂 Dataset loading & exploratory analysis
- [x] 🏗️ Feature engineering (success flag, daily counts)
- [x] 🎲 Bernoulli distribution — transaction success probability
- [x] 🔢 Binomial distribution — weekly transaction count modelling
- [x] 📅 Poisson distribution — daily transaction rate fitting
- [x] 📈 Log-Normal distribution — transaction amount fitting
- [x] 🔗 Power Law distribution — heavy tail analysis
- [x] 📉 Q-Q Plot — normality testing (raw + log-transformed)
- [x] 🔄 Box-Cox Transformation — variance stabilisation
- [x] 🎯 Z-Score analysis — P(amount > ₹5000) + outlier detection
- [x] 📊 PDF & CDF — full probability curve plots
- [x] 🏆 Best-fit comparison — KS test across 5 distributions

---

## ✅ Results Summary

| Analysis | Key Finding | Verdict |
|---|---|---|
| 🎲 Bernoulli | p = 0.427 success probability | ✅ 42.7% transactions succeed |
| 📅 Poisson | λ = 7.1 transactions/day | ✅ Mean = Variance confirmed |
| 📈 Log-Normal | μ=7.94, σ=0.59 (log scale) | ✅ Best fit for amounts |
| 🔗 Power Law | α ≈ 2.5 (heavy tail) | ✅ Pareto effect present |
| 📉 Q-Q Plot | Log amounts → near linear | ✅ Log-Normal confirmed |
| 🔄 Box-Cox | Optimal λ ≈ 0.15 | ✅ Skewness reduced |
| 🎯 Z-Score | P(X > ₹5000) ≈ 13.4% | ✅ Matches actual 13.2% |
| 🏆 Best Fit | Log-Normal wins KS test | ✅ Highest p-value |

---

## 🚀 How to Run

### 📋 Prerequisites

```bash
pip install pandas numpy scipy statsmodels matplotlib seaborn jupyter
```

### 🛠️ Step-by-Step

**Step 1 — Clone the repository**
```bash
git clone https://github.com/meet6949/spread-locator.git
cd spread-locator
```

**Step 2 — Place the dataset in the project folder**
```
spread-locator/
└── spread_locator_dataset.csv    ← put your CSV here
```

**Step 3 — Launch Jupyter Notebook**
```bash
jupyter notebook Spread_Locator_Analysis.ipynb
```

**Step 4 — Run All Cells**
```
Kernel → Restart & Run All
```
> Or press `Shift + Enter` to run cell by cell. All 8 plots save automatically as `.png` files.

---

## 📁 File Structure

```
📦 spread-locator/
│
├── 📓 Spread_Locator_Analysis.ipynb       ← Main Jupyter Notebook (Part B)
├── 📊 spread_locator_dataset.csv          ← 220 transaction records × 7 features
│
├── 📈 Generated Plots
│   ├── plot_00_overview.png
│   ├── plot_01_bernoulli_binomial.png
│   ├── plot_02_poisson.png
│   ├── plot_03_lognormal_powerlaw.png
│   ├── plot_04_qqplot.png
│   ├── plot_05_boxcox.png
│   ├── plot_06_zscore.png
│   ├── plot_07_pdf_cdf.png
│   └── plot_08_bestfit.png
│
└── 📄 README.md                           ← This file (Theory + Overview)
```

---

## 🧠 Key Concepts Quick Reference

```
📌 Statistical Distribution  →  Pattern describing how values are spread
📌 Q-Q Plot                  →  Visual normality test — points on diagonal = fits
📌 Discrete Distribution     →  Countable values (PMF) — Bernoulli, Binomial, Poisson
📌 Continuous Distribution   →  Uncountable values (PDF/CDF) — Normal, Log-Normal
📌 Bernoulli                 →  Single trial, two outcomes; P(success) = p
📌 Binomial                  →  n trials; E[X] = np, Var[X] = np(1−p)
📌 Poisson                   →  Count events over time; E[X] = Var[X] = λ
📌 Log-Normal                →  ln(X) is normal; ideal for financial amounts
📌 Power Law                 →  Heavy tail; P(X>x) ∝ x^(−α); Pareto 80-20 rule
📌 Box-Cox Transform         →  Power family (λ); stabilises variance, reduces skew
📌 Z-Score                   →  (X−μ)/σ; standardise data; detect outliers
📌 PDF                       →  Density at a point; area under curve = probability
📌 CDF                       →  P(X ≤ x); S-shaped; reads cumulative probability
📌 KS Test                   →  Goodness-of-fit: compares sample vs theoretical CDF
```

---

## 📌 Assumptions

1. Significance level **α = 0.05** used throughout
2. Log-Normal fit uses MLE parameters from log-transformed data
3. Power Law α estimated via log-log CCDF linear regression
4. Box-Cox requires strictly positive values — all amounts are positive ✓
5. KS test used for distribution comparison (non-parametric, distribution-free)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" width="100%"/>

**Made with ❤️ by [Meet Gajera](https://github.com/meet6949)**

*Spread Locator — Where Every Distribution Tells a Story*

⭐ *If this project helped you, consider giving it a star!* ⭐

</div>
