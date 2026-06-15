# Calculative Foundation

A Linear Algebra based project analyzing academic performance data using Python.

---

## About the Project

This project applies core Linear Algebra techniques on an academic score dataset to find meaningful patterns in student performance. It covers vector operations, matrix computations, decompositions and dimensionality reduction methods.

---

## Dataset

**File:** `academic_scores.csv`

| Column | Description |
|---|---|
| ID | Unique student ID |
| Physics | Physics score |
| Chemistry | Chemistry score |
| Biology | Biology score |
| Geography | Geography score |
| Arts | Arts score |
| Total_Score | Sum of all subject scores |
| Performance | High or Low based on average |

> 200 student records generated for this project.

---

## Files in this Repository

```
calculative-foundation/
│
├── academic_scores.csv                  # Dataset
├── Calculative_Foundation_Friend.ipynb  # Jupyter Notebook
├── Code_Implementation_Friend.pdf       # Implementation Report
└── README.md                            # Documentation
```

---

## What's Covered

### Part A - Vectors
- Student scores as vectors
- Norm-1 and Norm-2
- Dot product and angle
- Cross product (3D)
- Vector projection

### Part B - Matrix Operations
- Building a score matrix
- Matrix addition and multiplication
- Transpose, Inverse and Determinant

### Part C - Geometry
- Line, Plane and Hyperplane from dataset
- 2D to 3D to 5D dimensionality explained

### Part D - Decomposition
- Eigenvalues and Eigenvectors of covariance matrix
- LU Decomposition
- SVD with singular values

### Part E - Dimensionality Reduction
- PCA from 5D to 2D with variance explained
- LDA for High vs Low performance classification

---

## Libraries Used

- `pandas` - data handling
- `numpy` - linear algebra operations
- `matplotlib` - visualization
- `scipy` - LU decomposition
- `sklearn` - PCA and LDA

---

## Key Findings

- PCA reduces 5 subject dimensions to 2 while retaining most variance
- LDA clearly separates High and Low performing students
- Eigenvalues show which subjects vary most across students
- SVD reveals dominant patterns in the academic score data

---
