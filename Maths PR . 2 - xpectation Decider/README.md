# 🎯 Expectation Decider Project

> Probability + Statistics based student performance analysis project

---

# 📌 Why I Made This Project?

Is project ka goal tha student ke exam pass hone ki probability analyze karna using:

- Study Hours
- Attendance
- Group Discussion
- Previous Test Score

Basically ye check karna tha:

> "Kaunse factors student ke pass hone ko affect karte hai?"

Maine probability, statistics aur visualization use karke analysis kiya.

---

# 📂 Dataset Information

Dataset me 200 students ka data hai.

### Columns

| Column Name | Meaning |
|---|---|
| study_hours | Week me kitne hours study ki |
| attendance | Lecture attendance percentage |
| group_discussion | Group discussion me participate kiya ya nahi |
| previous_test_score | Previous internal exam marks |
| final_exam_pass | Final exam me pass/fail |

---

# 🧠 Concepts Covered in This Project

Ye project mainly probability aur statistics ke concepts par based tha:

1. Probability Basics
2. Types of Events
3. Empirical vs Theoretical Probability
4. Random Variable
5. Probability Distribution
6. Mean & Variance
7. Venn Diagram
8. Contingency Table
9. Joint / Marginal / Conditional Probability
10. Independent vs Dependent Events
11. Bayes Theorem

---

# 1️⃣ Probability Basics

## What is Probability?

Probability matlab:

> kisi event ke hone ki possibility kitni hai

Range:

```text
0 → impossible
1 → certain
```

Formula:

```text
P(E) = Favorable Outcomes / Total Outcomes
```

### Example from dataset

Student pass hone ki probability:

```text
P(Pass)
=
No. of students passed
----------------------
Total students
```

---

## Important Terminology

### Experiment

Koi activity jisme outcome mile.

Example:

Exam conduct karna.

---

### Outcome

Experiment ka result.

Example:

```text
Pass
Fail
```

---

### Event

Specific condition.

### Example Events

Event 1:

Student studies >10 hours/week

Event 2:

Attendance >80%

Event 3:

Student participated in discussion AND passed exam

---

### Sample Space

All possible outcomes.

Example:

```text
S = {Pass, Fail}
```

---

# 2️⃣ Types of Probability

## A. Empirical Probability

### Meaning

Real dataset use karke probability nikalna.

Formula:

```text
P(E)
=
Favorable Outcomes
-------------------
Total Outcomes
```

### Example

Pass probability:

```text
Students Passed / Total Students
```

### Why Used?

Kyuki hamare paas actual student dataset available tha.

---

## B. Theoretical Probability

### Meaning

Mathematical assumption based probability.

Example:

Agar pass/fail equally likely ho:

```text
P(Pass)=1/2
```

---

# 3️⃣ Random Variable

## What is Random Variable?

Random value jo chance par depend karti ho.

### Example used in project

```text
X = Number of students passing out of 3 randomly selected students
```

Possible values:

```text
0
1
2
3
```

---

# 4️⃣ Probability Distribution

Probability distribution table banayi thi.

Purpose:

```text
Har outcome ki probability dekhna
```

Example:

| X | Probability |
|---|---|
| 0 | P(X=0) |
| 1 | P(X=1) |
| 2 | P(X=2) |
| 3 | P(X=3) |

---

## Mean of Random Variable

Formula:

```text
E(X)=ΣxP(x)
```

Meaning:

Average expected value.

---

## Variance

Formula:

```text
Var(X)=E(X²)-[E(X)]²
```

Meaning:

Data kitna spread hai.

---

# 5️⃣ Venn Diagram

## Why Used?

Overlap check karne ke liye.

### Set A

Students studying:

```text
>10 hours/week
```

### Set B

Students with:

```text
Attendance >80%
```

### Overlap

Students satisfying both conditions.

---

# 6️⃣ Contingency Table

Comparison kiya between:

```text
group_discussion
VS
final_exam_pass
```

Purpose:

Check karna:

> discussion participation pass hone me help karti hai ya nahi

---

## Joint Probability

Meaning:

Dono events ek saath hone ki probability.

Example:

```text
Student participates in discussion
AND
passes exam
```

Formula:

```text
P(A ∩ B)
```

---

## Marginal Probability

Single event ki probability.

Example:

```text
P(Pass)
```

---

## Conditional Probability

Meaning:

Ek event hone par dusre ki probability.

Example:

```text
Probability of passing
given student participated in discussion
```

Formula:

```text
P(A|B)
=
P(A ∩ B)
---------
P(B)
```

---

# 7️⃣ Relationship Between Variables

Yaha check kiya:

```text
group_discussion
&
final_exam_pass
```

Independent hai ya dependent?

### Final Understanding

Dependent events lage because:

Discussion participation pass hone ko influence kar sakta hai.

Mutually exclusive nahi hai because:

Student discussion bhi kar sakta hai aur pass bhi ho sakta hai.

---

# 8️⃣ Bayes Theorem

## Why Used?

Ye calculate karne ke liye:

> High attendance hone par pass hone ki probability kitni hai?

Given:

```text
70% passing students had high attendance

40% failing students had high attendance

60% students had high attendance
```

Formula:

```text
P(A|B)
=
P(B|A) × P(A)
----------------
P(B)
```

Use:

```text
Probability of Pass
given High Attendance
```

---

# 📊 Visualizations Used

## Histogram

Study hours distribution dekhne ke liye.

---

## Scatter Plot

Attendance aur previous score ka relationship dekhne ke liye.

---

## Bar Chart

Pass vs fail comparison.

---

## Venn Diagram

High study + high attendance overlap.

---

## Heatmap

Feature relationship samajhne ke liye.

---

# 🛠️ Libraries Used

```python
pandas
numpy
matplotlib
seaborn
matplotlib-venn
```

Install:

```bash
pip install pandas numpy matplotlib seaborn matplotlib-venn
```

---

# 🚀 How to Run

### Open notebook

```text
Expectation_Decider_Project_Charts.ipynb
```

Run all cells.

---

# 📌 Key Learnings from This Project

Is project se maine sikha:

- Probability real dataset par kaise apply hoti hai
- Empirical vs theoretical probability
- Conditional probability practically kaise use hoti hai
- Bayes theorem ka real use case
- Venn diagram probability me kaise useful hai
- Contingency table se relationship kaise check karte hai
- Statistical visualization ka use

---

# 🏁 Final Conclusion

Analysis ke hisab se:

### Factors increasing pass probability:

✅ Higher study hours

✅ Better attendance

✅ Group discussion participation

✅ Good previous test score

Conclusion:

> Consistent study + good attendance + participation = higher chance of passing exam

---



# 📊 Visualizations Used

---

## 1️⃣ Final Exam Pass Distribution (Bar Chart)

This graph shows

 Kitne students pass hue aur kitne fail hue.

![Pass Fail Distribution](imagespass_fail_distribution.png)

### 📌 Observation

- Pass students zyada hai
- Fail students comparatively kam hai

### 🧠 What I Learned

Dataset me majority students pass hue, iska matlab generated dataset me passing probability higher rakhi gayi hai.

---

## 2️⃣ Study Hours Distribution (Histogram)

Purpose

 Students generally kitna study karte hai dekhna.

![Histogram](imagesstudy_hours_histogram.png)

### 📌 Observation

- Most students middle range study hours me hai

### 🧠 What I Learned

Study pattern aur spread samajhne me help milti hai.

---

## 3️⃣ Attendance vs Previous Score (Scatter Plot)

Purpose

 Attendance aur previous test score ka relationship check karna.

![Scatter Plot](imagesattendance_vs_score.png)

### 📌 Observation

- Higher attendance wale students ka score generally better tha.

### 🧠 What I Learned

Attendance academic performance ko influence kar sakti hai.

---

## 4️⃣ Venn Diagram

Purpose

 Overlap check karna between

- Students studying 10 hours
- Students attendance 80%

![Venn Diagram](imagesvenn_diagram.png)

### 📌 Observation

Overlap students both conditions satisfy karte hai.

### 🧠 What I Learned

Intersection probability practically samaj aayi.

---

## 5️⃣ Correlation Heatmap

Purpose

 Variables ka relationship samajhna.

![Heatmap](imagescorrelation_heatmap.png)

### 📌 Observation

Kis feature ka exam result par zyada impact hai wo visible hota hai.

### 🧠 What I Learned

Feature relationships visually samajhne me easy hua.


## 👨‍💻 Made By

**Meet Gajera**