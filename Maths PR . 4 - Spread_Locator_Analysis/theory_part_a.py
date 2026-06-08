# ============================================================
# SPREAD LOCATOR – Part A: Theoretical Foundation
# Statistical Distributions & Probability Concepts
# ============================================================

# ──────────────────────────────────────────────────────────────
# 1. What is Statistical Distribution?
# ──────────────────────────────────────────────────────────────
"""
A statistical distribution is a function that describes all the
possible values a random variable can take and how likely each
value (or range of values) is to occur.

Think of it like this: if I record the daily transaction amounts
from an e-commerce platform for a year, the pattern in which
those values appear — what's common, what's rare, where the
data "clusters" — is its distribution.

Types at a glance:
  • Discrete distributions  → countable outcomes (no. of orders per day)
  • Continuous distributions → uncountable outcomes (transaction amount)

Key parameters that define a distribution:
  • Mean (μ)    – central tendency / expected value
  • Variance (σ²) – spread / how much values deviate from mean
  • Skewness   – asymmetry (right-skewed = long tail on right)
  • Kurtosis   – tail heaviness

Why it matters in our project:
  Understanding which distribution fits our transaction amounts
  helps us make probability-based business decisions:
  "What % of orders exceed ₹5000?" is answerable only if we
  know the distribution.
"""

# ──────────────────────────────────────────────────────────────
# 2. What is a Q-Q Plot and Why is it Used?
# ──────────────────────────────────────────────────────────────
"""
Q-Q stands for Quantile-Quantile. It is a diagnostic plot used
to compare two probability distributions by plotting their
quantiles against each other.

Most commonly, we compare our sample data against the
theoretical normal distribution.

How to read it:
  • X-axis → Theoretical quantiles (what normal distribution predicts)
  • Y-axis → Sample quantiles (what our data actually shows)
  • If the points fall perfectly along the 45° diagonal line,
    the data follows that distribution.
  • Curved/bent tails → skewness or heavy tails (not normal)
  • Systematic S-curve → different kurtosis

In our project:
  • Raw transaction amounts bend upward at the right tail
    → right-skewed, NOT normal.
  • After log transformation the Q-Q plot is nearly linear
    → confirming Log-Normal behaviour.

Why we use it over just looking at a histogram:
  A histogram's shape depends on bin size. Q-Q plots are
  bin-independent and far more sensitive to distributional
  differences in the tails.
"""

# ──────────────────────────────────────────────────────────────
# 3. Difference Between Discrete and Continuous Distributions
# ──────────────────────────────────────────────────────────────
"""
DISCRETE DISTRIBUTIONS
  Definition  : Random variable takes countable, distinct values.
  Examples    : Number of transactions in a day (0, 1, 2, …)
                Number of defective items in a batch
  Probability : Described by PMF (Probability Mass Function)
                → P(X = k) gives the probability at each exact value
  Examples of distributions:
    - Bernoulli, Binomial, Poisson, Geometric, Hypergeometric

CONTINUOUS DISTRIBUTIONS
  Definition  : Random variable can take any value in an interval.
                Infinitely many possible values.
  Examples    : Transaction amount (₹1234.56 or ₹1234.57 or anything)
                Height, time, temperature
  Probability : Described by PDF (Probability Density Function)
                → P(X = exactly k) = 0; we calculate P(a ≤ X ≤ b)
  Examples of distributions:
    - Normal, Log-Normal, Exponential, Gamma, Beta, Weibull

Key differences in a table:
  Feature           | Discrete              | Continuous
  ─────────────────────────────────────────────────────
  Values            | Countable             | Uncountable
  Probability tool  | PMF                   | PDF
  P(X = exact k)    | Defined, can be > 0   | Always = 0
  Example metric    | Daily orders           | Order amount (₹)
  Visualisation     | Bar chart              | Histogram / Curve

In our dataset:
  • transaction_count → Discrete (Binomial/Poisson)
  • transaction_amount → Continuous (Log-Normal)
  • transaction_status → Discrete/Binary (Bernoulli)
"""

# ──────────────────────────────────────────────────────────────
# 4. What is Bernoulli Distribution?
# ──────────────────────────────────────────────────────────────
"""
The Bernoulli distribution is the simplest discrete probability
distribution. It models a single experiment (called a Bernoulli trial)
that has exactly two outcomes:
  → Success (1) with probability p
  → Failure (0) with probability (1 − p)

PMF:
  P(X = 1) = p
  P(X = 0) = 1 − p

Parameters:
  p ∈ [0, 1] — probability of success

Statistics:
  Mean     E[X] = p
  Variance Var[X] = p(1 − p)

Real-life example:
  Tossing a coin: p = 0.5 for heads.

In our project:
  Each transaction is a Bernoulli trial:
    Success = transaction_status == "Success"
    p = 0.427 (approx. 42.7% transactions succeed)
  
  So P(a randomly picked transaction succeeds) = 0.427

Why useful:
  It forms the building block for more complex distributions:
  Binomial = n independent Bernoulli trials summed together.
"""

# ──────────────────────────────────────────────────────────────
# 5. What is Binomial Distribution?
# ──────────────────────────────────────────────────────────────
"""
The Binomial distribution models the number of successes in
n independent Bernoulli trials, each with the same probability p.

PMF:
  P(X = k) = C(n, k) × p^k × (1−p)^(n−k)

Where:
  n = number of trials
  k = number of successes we are calculating probability for
  p = probability of success in each trial
  C(n,k) = n! / (k! × (n−k)!) — "n choose k"

Parameters:
  n (positive integer), p ∈ [0, 1]

Statistics:
  Mean     E[X] = np
  Variance Var[X] = np(1 − p)

Real-life example:
  A quality inspector checks 20 items from a batch where each
  item has a 5% defect rate. X ~ Binomial(20, 0.05).

In our project:
  Each customer can make up to `transaction_count` transactions
  in a week. Each transaction has p ≈ 0.427 chance of success.
  X ~ Binomial(n = max_transaction_count, p = 0.427)
  
  This tells management: "Out of a customer's weekly transactions,
  how many are expected to succeed?"

Note: When n → ∞ and p → 0 such that np = λ stays constant,
  Binomial(n,p) → Poisson(λ). This is the Poisson Limit Theorem.
"""

# ──────────────────────────────────────────────────────────────
# 6. Explain Log-Normal Distribution
# ──────────────────────────────────────────────────────────────
"""
A random variable X follows a Log-Normal distribution if its
natural logarithm (ln X) follows a Normal distribution.

In other words: if Y = ln(X) ~ Normal(μ, σ²), then X ~ Log-Normal(μ, σ).

PDF:
  f(x) = [1 / (xσ√(2π))] × exp[−(ln x − μ)² / (2σ²)]   for x > 0

Parameters:
  μ — mean of the log-transformed variable
  σ — std deviation of the log-transformed variable

Statistics:
  Mean     E[X] = exp(μ + σ²/2)
  Variance Var[X] = (exp(σ²) − 1) × exp(2μ + σ²)
  Mode     = exp(μ − σ²)

Characteristics:
  • Always positive (x > 0) — perfect for prices/amounts!
  • Right-skewed (long tail towards large values)
  • After log transformation → becomes normal (great for modelling)
  • Products of many small independent factors → Log-Normal
    (by the Multiplicative Central Limit Theorem)

Real-life examples:
  Income distributions, stock prices, insurance claim amounts,
  city populations, e-commerce transaction amounts.

In our project:
  transaction_amount follows Log-Normal because:
  1. Amounts are always positive (₹ > 0)
  2. Histogram is right-skewed
  3. log(amount) histogram looks approximately normal
  4. Q-Q plot of log(amount) aligns with normal reference line
  5. KS test confirms Log-Normal is the best fit
"""

# ──────────────────────────────────────────────────────────────
# 7. Explain Power Law Distribution
# ──────────────────────────────────────────────────────────────
"""
A Power Law distribution (also called Pareto distribution in
many applications) is one where the probability of a value x
follows:
  P(X > x) ∝ x^(−α)     (CCDF / Survival function)
  f(x) ∝ x^(−α−1)       (PDF)

Where α > 0 is the scaling exponent (tail index).

Key properties:
  • Heavy tails — extreme values are much more probable than
    Normal or Exponential distributions predict.
  • Scale-free: the ratio of probabilities depends only on the
    ratio of values, not their absolute magnitude.
  • No finite mean if α ≤ 1; no finite variance if α ≤ 2.

How to detect a Power Law:
  → Plot log(P(X > x)) vs log(x); if it's a straight line, the
    slope equals −α.

Famous examples:
  • Pareto Principle (80-20 rule): top 20% customers generate 80% revenue
  • Wealth distribution (Pareto)
  • City sizes (Zipf's law)
  • Word frequency in language
  • Website traffic (most sites have very few visitors)

In our project:
  Fitting a Power Law to transaction amounts shows a heavy tail.
  This means a small fraction of high-value orders contribute
  disproportionately to total revenue — classic e-commerce behaviour.
  α ≈ 2.5 in our data suggests finite mean and variance exist.
"""

# ──────────────────────────────────────────────────────────────
# 8. What is Box-Cox Transformation?
# ──────────────────────────────────────────────────────────────
"""
Box-Cox is a family of power transformations that transforms
non-normal data into approximately normal data, and
stabilises variance across different ranges.

Formula:
  y(λ) = (x^λ − 1) / λ    if λ ≠ 0
  y(λ) = ln(x)             if λ = 0

Here λ (lambda) is a parameter estimated from the data itself
(using maximum likelihood estimation) to find the best
normalising transformation.

Special cases:
  λ = 1   → No transformation (y = x)
  λ = 0   → Log transformation (y = ln x)
  λ = 0.5 → Square root transformation
  λ = −1  → Reciprocal transformation

Requirements:
  • Data must be strictly positive (x > 0) before applying Box-Cox
    (use Yeo-Johnson transform for zero/negative values)

Why use it:
  1. Many statistical tests (t-test, ANOVA, regression) assume
     normality. Box-Cox brings data closer to normal.
  2. Stabilises variance (heteroscedasticity → homoscedasticity)
  3. Makes the distribution symmetric, reducing skew

In our project:
  Optimal λ ≈ 0.1–0.3 (close to 0), confirming log transformation
  is near-optimal. Box-Cox further reduces skewness compared to
  raw data, making transaction_amount ready for regression analysis.
"""

# ──────────────────────────────────────────────────────────────
# 9. Explain Poisson Distribution with an Example
# ──────────────────────────────────────────────────────────────
"""
The Poisson distribution models the number of events that
occur in a fixed interval of time or space, given:
  1. Events occur independently
  2. Average rate (λ) is constant
  3. Two events cannot occur at exactly the same instant

PMF:
  P(X = k) = (e^(−λ) × λ^k) / k!

Parameter:
  λ (lambda) > 0 — average number of events per interval

Statistics:
  Mean     E[X] = λ
  Variance Var[X] = λ          (mean = variance is unique to Poisson!)

Classic example:
  A hospital receives on average λ = 4 emergency calls per hour.
  What is the probability of exactly 7 calls in an hour?
  P(X=7) = (e^(−4) × 4^7) / 7! = 0.0595 → about 6%

Other examples:
  • Number of traffic accidents at an intersection per month
  • Number of typos per page of a book
  • Requests to a web server per second

In our project:
  Daily transaction count follows Poisson(λ ≈ 7) because:
  • Transactions arrive independently
  • Rate is roughly constant across January
  • It's a count variable over a fixed time window (1 day)
  
  This is used to predict: "On how many days this month will
  we see more than 10 transactions?" → P(X > 10) = 1 − F(10)
"""

# ──────────────────────────────────────────────────────────────
# 10. What is Z-Score Probability?
# ──────────────────────────────────────────────────────────────
"""
A Z-Score (also called standard score) measures how many
standard deviations a data point is from the mean:

  Z = (X − μ) / σ

Where:
  X = individual data point
  μ = population mean
  σ = population standard deviation

Properties:
  • Z = 0   → value equals the mean
  • Z = 1   → value is 1 std dev above mean
  • Z = −2  → value is 2 std devs below mean
  • Z > 3 or Z < −3 → typically considered outlier (< 0.3% of data)

Z-score probabilities (from standard normal table):
  P(Z < 1.96) ≈ 0.975   → 95% confidence interval uses ±1.96
  P(Z < 2.58) ≈ 0.995   → 99% confidence interval uses ±2.58
  P(−1 < Z < 1) ≈ 0.683  → 68-95-99.7 empirical rule

How we use it for probability:
  P(X > threshold) = P(Z > z_threshold) = 1 − Φ(z_threshold)
  Where Φ is the standard normal CDF.

In our project:
  For threshold = ₹5000:
  z = (5000 − mean) / std = z_value
  P(amount > ₹5000) = 1 − Φ(z)

Applications:
  • Detecting unusual transactions (outlier fraud detection)
  • Setting premium/discount thresholds
  • Comparing performance across regions (normalised metric)
"""

# ──────────────────────────────────────────────────────────────
# 11. Differentiate PDF and CDF
# ──────────────────────────────────────────────────────────────
"""
PDF — Probability Density Function (for continuous distributions)
CDF — Cumulative Distribution Function

PDF:
  • Describes the relative likelihood of a continuous random
    variable taking a specific value.
  • f(x) ≥ 0 for all x
  • Area under the entire PDF curve = 1
  • P(a ≤ X ≤ b) = ∫[a to b] f(x) dx
  • P(X = exact value) = 0 (point probability is always zero)
  • Shape: bell curve (Normal), right-skewed curve (Log-Normal),
    exponential decay (Exponential), etc.

CDF:
  • F(x) = P(X ≤ x) — probability that variable is at most x
  • Always non-decreasing: F(−∞) = 0, F(+∞) = 1
  • F'(x) = f(x) — derivative of CDF gives back PDF
  • Shape: always S-shaped / monotonically increasing from 0 to 1

Comparison table:
  Feature        | PDF                          | CDF
  ───────────────────────────────────────────────────────────
  Question answered | How dense is probability at x? | P(X ≤ x)?
  Range          | 0 to ∞                       | 0 to 1
  Shape          | Varies (bell, skewed, etc.)  | Always S-shaped
  Usage          | Visualise distribution shape | Compute probabilities
  P(a < X < b)   | Area under curve from a to b | F(b) − F(a)

Relationship:
  CDF(x) = ∫[−∞ to x] PDF(t) dt
  PDF(x) = d/dx CDF(x)

In our project:
  • PDF helps us see that most transactions cluster between
    ₹1,000–₹4,000.
  • CDF gives us actionable answers:
    - "What % of transactions are below ₹3,000?" → Read F(3000)
    - "What's the ₹ value where 90% of transactions fall below?" → Inverse CDF
"""

print("Part A – Theory notes complete.")
print("All 11 topics covered with definitions, formulas,")
print("properties, and project-specific applications.")
