# 📚 Part A — Theory Short Answers

> Statistics & Linear Algebra — Final Exam | Short Question Answers

---

### Q1. 📊 Explain Mean, Median, and Mode with a real-life example.

**Mean** is the average of all values — add everything up and divide by the count.
**Median** is the middle value when data is sorted in order.
**Mode** is the value that appears most frequently.

**Real-life example:** Consider monthly salaries of 5 employees: ₹20K, ₹25K, ₹30K, ₹30K, ₹100K.
- Mean = ₹41K (pulled high by one rich employee — misleading!)
- Median = ₹30K (middle value — more realistic)
- Mode = ₹30K (most common salary)

This shows why median is better than mean when data has extreme values (outliers).

---

### Q2. 📐 What is the difference between Variance and Standard Deviation?

**Variance** measures how far each data point is from the mean, on average — but the result is in **squared units**, which makes it hard to interpret directly.

**Standard Deviation (SD)** is simply the **square root of variance**, bringing it back to the original unit.

**Example:** If exam scores have a variance of 225, the standard deviation is √225 = 15 marks — which is much easier to understand. Both tell you how "spread out" the data is, but SD is more intuitive.

---

### Q3. 🔔 Define Normal Distribution and give one practical use case.

A **Normal Distribution** is a bell-shaped, symmetric distribution where most data clusters around the mean, and values taper off equally on both sides. It follows the **68-95-99.7 rule** (68% data within 1 SD, 95% within 2 SD, 99.7% within 3 SD).

**Practical use case:** Human heights in a population follow a normal distribution. Most people are of average height, very few are extremely tall or extremely short — a perfect bell curve.

---

### Q4. 📉 Explain Skewness and Kurtosis in simple words.

**Skewness** tells us whether the data is **tilted (asymmetric)**:
- Positive skew → tail on the right (more low values, few very high ones)
- Negative skew → tail on the left
- Zero skew → perfectly symmetric (normal distribution)

**Kurtosis** tells us how **peaked or flat** the distribution is:
- High kurtosis → sharp peak, heavy tails (more extreme values)
- Low kurtosis → flat peak, light tails

**Simple analogy:** Skewness = "is the slide tilted?" | Kurtosis = "is the peak sharp or flat?"

---

### Q5. 🎲 What is Probability? Differentiate between Empirical vs Theoretical Probability.

**Probability** is a number between 0 and 1 that represents how likely an event is to occur. 0 = impossible, 1 = certain.

| | Theoretical Probability | Empirical Probability |
|---|---|---|
| **Based on** | Logic / math | Actual experiments |
| **Formula** | Favorable outcomes / Total outcomes | Observed frequency / Total trials |
| **Example** | P(Heads) = 1/2 (by theory) | Flip a coin 100 times → 48 heads → P = 0.48 |

As the number of experiments increases, empirical probability **converges** to theoretical probability (Law of Large Numbers).

---

### Q6. 🔗 Explain Independent vs Dependent Events with one example each.

**Independent Events:** The outcome of one event does **not affect** the other.
- **Example:** Rolling a dice and flipping a coin — getting a 6 on the dice does not change the probability of getting heads.
- P(A and B) = P(A) × P(B)

**Dependent Events:** The outcome of one event **does affect** the other.
- **Example:** Drawing cards from a deck without replacement — after drawing an Ace, the probability of drawing another Ace changes (3/51 instead of 4/52).
- P(A and B) = P(A) × P(B | A)

---

### Q7. 🧠 What is the intuition of Bayes' Theorem in daily life?

**Bayes' Theorem** says: *update your belief when you get new evidence.*

**Daily life example:** Suppose you test positive for a rare disease. The test isn't perfect — it has a 5% false positive rate. Bayes' Theorem helps you calculate the *real* probability that you actually have the disease, by factoring in:
- How rare the disease is (prior probability)
- How accurate the test is (likelihood)

**Intuition:** Don't panic at a positive test — if the disease is very rare, even a positive result might mean you're likely fine. Always update beliefs with evidence.

---

### Q8. 🔢 Explain Eigenvalue and Eigenvector in simple terms.

Imagine you have a transformation (like stretching or rotating space). Most vectors change direction when transformed — but **Eigenvectors** are special vectors that **only get scaled** (stretched or shrunk), never rotated.

The **Eigenvalue** is the **scaling factor** — how much the eigenvector got stretched or compressed.

**Simple analogy:** If you stretch a rubber band along the x-axis, the x-direction is an eigenvector (it stays in the same direction), and how much it stretched is the eigenvalue.

**Real-world use:** PCA (Principal Component Analysis) in Machine Learning uses eigenvectors to find the most important directions in data — used for dimensionality reduction.

---

*End of Part A — Theory Answers*
