# Calculative Foundation Project

> A comprehensive application of linear algebra concepts to student academic score data — from raw vectors to dimensionality reduction.

![Linear Algebra](https://img.shields.io/badge/Linear%20Algebra-5C6BC0?style=flat-square)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-1B9E75?style=flat-square)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-2196F3?style=flat-square)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

---

## Overview

| Metric | Value |
|---|---|
| Students | 200 |
| Subjects (dimensions) | 5 |
| LA concepts applied | 9 |
| Output components (PCA) | 2 |

Each student's scores across 5 subjects form a 5-dimensional vector. This project applies foundational linear algebra operations — norms, matrix decompositions, eigenanalysis, and dimensionality reduction — to explore and visualize academic performance patterns.

---

## Concepts

### Vectors

A vector represents a student's scores as an ordered list of numbers. Each student has 5 subject scores forming a 5-dimensional vector. Two vectors can be compared using dot product and the angle between them. Cross product is used for 3D vectors to find a perpendicular direction. Projection shows how much one student vector aligns with another.

**Examples**

```
S001 = [61, 94, 75, 89, 56]
dot(S001, S002) = 61×74 + 94×53 + 75×82 + 89×49 + 56×63
```

---

### Norms

Norm gives the overall size or length of a score vector. L1 norm adds up all the absolute score values. L2 norm finds the straight-line distance from origin to the score point. Higher norm means the student has higher overall scores. Used to compare and normalize student score vectors.

**Examples**

```
L1([61, 94, 75, 89, 56]) = 375
L2([3, 4]) = √(9 + 16) = 5
```

---

### Matrix Operations

Scores of multiple students form a matrix with rows as students and columns as subjects. Matrix addition combines scores of two groups element by element. Matrix multiplication computes similarity scores between groups. Transpose swaps rows and columns, converting student-wise to subject-wise view. Inverse exists only when the determinant is non-zero.

**Examples**

```
Adding scores of student groups → combined performance matrix
det(M) ≠ 0 → matrix is invertible
```

---

### Linear Transformations & Geometry

One subject score (e.g. Physics) represents a 1D line. Two subjects form a 2D plane. Three subjects create a 3D space. All 5 subjects together form a 5-dimensional hyperplane. Each subject added increases the number of dimensions by one.

**Examples**

```
Physics scores alone → number line (1D)
Physics vs Chemistry scatter plot → 2D plane
```

---

### Eigenvalues & Eigenvectors

Computed from the covariance matrix of the academic score data. Eigenvectors point in the directions of maximum data spread. Eigenvalues tell us how much variance exists in each direction. Subjects with higher eigenvalue contribution vary more across students. They form the mathematical basis for PCA dimensionality reduction.

**Examples**

```
5 subjects → 5 eigenvalues and eigenvectors
Largest eigenvalue = direction of greatest score variance
```

---

### LU Decomposition

Splits the score matrix into a lower triangular L and upper triangular U matrix. A permutation matrix P handles row reordering during decomposition. Makes solving linear systems faster and more numerically stable. Useful for repeated solving with the same matrix but different right-hand sides. Applied on the first 5 students' score matrix in this project.

**Examples**

```
M = P × L × U
L has ones on diagonal; U has non-zero upper values
```

---

### Singular Value Decomposition (SVD)

Breaks the full score matrix into three matrices U, S, and Vᵀ. S contains singular values sorted from largest to smallest. Larger singular values capture more important patterns in the data. Keeping only top singular values reduces dimensions while retaining key information. Widely applied in image compression and recommendation engines.

**Examples**

```
Score matrix (200×5) → 5 singular values
First singular value >> rest → one dominant pattern
```

---

### PCA — Principal Component Analysis

Reduces 5 subject scores to 2 principal components for visualization. New components are linear combinations of original subject scores. First component captures the direction of maximum score variance. Does not need class labels — works on raw score data directly. Helps identify clusters of high and low performing students visually.

**Examples**

```
200 students × 5D → 200 students × 2D
PCA scatter plot separates High and Low performers into visible clusters
```

---

### LDA — Linear Discriminant Analysis

Supervised method that uses class labels (High / Low) to find the best separation axis. Finds a single axis that maximises distance between High and Low groups. Projects 5D score data onto 1D while keeping class separation intact. More effective than PCA for classification tasks with labeled data.

**Examples**

```
avg score > 70 → labeled High, otherwise Low
5D scores → 1 discriminant value that best splits both groups
```

---

## Dimensionality Pipeline

```
Raw scores (5D)
    │
    ▼
Covariance matrix
    │
    ▼
Eigen decomposition
    │
    ├──▶ PCA → 2D visualization (unsupervised)
    │
    └──▶ LDA → 1D separator (supervised, uses class labels)
```

---

## Key Distinction

| Method | Type | Input | Output | Goal |
|---|---|---|---|---|
| PCA | Unsupervised | Raw scores | 2 components | Maximise variance |
| LDA | Supervised | Scores + labels | 1 discriminant | Maximise class separation |

---

*End of Report*
