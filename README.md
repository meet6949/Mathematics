<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=Calculative%20Foundation&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Linear%20Algebra%20Concepts%20%26%20Theory%20for%20Data%20Science&descAlignY=55&descSize=17" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Math](https://img.shields.io/badge/Math-LaTeX-543C8F?style=for-the-badge&logo=latex&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-22c55e?style=for-the-badge)]()

<br/>

> *✨ "Every dataset is a matrix. Every pattern is a transformation. Every insight begins with a vector." ✨*

<br/>

**📖 Reading Time:** ~30 Mins &nbsp;&nbsp;**|**&nbsp;&nbsp; **🧪 Type:** Theory Reference &nbsp;&nbsp;**|**&nbsp;&nbsp; **🧮 Domain:** Linear Algebra

**👨‍💻 Author:** [Meet Gajera](https://github.com/meet6949)

<br/>

</div>

---

## 📌 Table of Contents

<details open>
<summary><b>Click to expand / collapse</b></summary>

- [🎯 Project Overview](#-project-overview)
- [🗂️ Document Structure](#️-document-structure)
- [📚 Theoretical Foundation](#-theoretical-foundation)
- [✅ Topics Covered](#-topics-covered)
- [🧠 Key Takeaways](#-key-takeaways)
- [🚀 How to Use This Guide](#-how-to-use-this-guide)
- [📁 File Structure](#-file-structure)
- [🧠 Key Concepts Quick Reference](#-key-concepts-quick-reference)
- [📌 Assumptions & Scope](#-assumptions--scope)

</details>

---

## 🎯 Project Overview

<table>
<tr>
<td>

This document is a **theoretical reference** covering the core Linear Algebra concepts that power the **Calculative Foundation** project. It walks through vectors, matrices, geometric subspaces, decompositions, and dimensionality-reduction techniques — the mathematical backbone behind most data science and machine learning algorithms.

**Covered here:**
- 🧭 Vectors, norms, and vector operations
- 🔲 Matrix operations, inverses, and determinants
- 🌐 Lines, planes, and hyperplanes
- 🧩 Eigen decomposition, LU decomposition, and SVD
- 📉 PCA and LDA for dimensionality reduction

**The goal:** Build the geometric and algebraic intuition needed to understand *how* and *why* these tools work — not just memorize formulas.

</td>
<td>

```
📊 Vectors & Matrices
         │
         ▼
🧭 Vector Operations
  (Norms, Dot, Cross, Projection)
         │
         ▼
🔲 Matrix Operations
  (Transpose, Inverse, Determinant)
         │
         ▼
🧩 Decompositions
  (Eigen, LU, SVD)
         │
         ▼
📉 Dimensionality Reduction
  (PCA, LDA)
         │
         ▼
✅ ML Models & Insights
```

</td>
</tr>
</table>

---

## 🗂️ Document Structure

> **Topics:** `11` &nbsp;|&nbsp; **Sections:** `5` &nbsp;|&nbsp; **Focus:** `Theory + Applications`

| # | Section | Concepts Covered | Core Tool |
|---|---------|-------------------|-----------|
| 1 | Vectors & Norms | L1 (Manhattan), L2 (Euclidean) | ‖x‖₁, ‖x‖₂ |
| 2 | Dot Product | Scalar similarity, orthogonality | A · B |
| 3 | Cross Product | Perpendicular vectors (3D only) | A × B |
| 4 | Vector Projection | Component decomposition | proj_B(A) |
| 5 | Matrix Operations | Addition, multiplication, transpose | A+B, AB, Aᵗ |
| 6 | Inverse & Determinant | Reversibility, scaling | A⁻¹, det(A) |
| 7 | Geometric Subspaces | Lines, planes, hyperplanes | ℝⁿ⁻¹ |
| 8 | Eigen Decomposition | Eigenvalues & eigenvectors | Av = λv |
| 9 | LU Decomposition | Triangular factorization | A = LU |
| 10 | SVD | Universal factorization | A = UΣVᵗ |
| 11 | Dimensionality Reduction | PCA, LDA | Covariance eigen-analysis |

---

## 📚 Theoretical Foundation

> 💡 **11 Core Concepts** — definitions, formulas, properties, and real-world applications.

<details>
<summary><b>1️⃣ Vectors & Norms</b> — Measuring magnitude and direction</summary>

<br/>

**Definition:** A vector is an ordered list of numbers representing both magnitude and direction. In data science, a single observation (e.g., a row of features) is represented as a vector in n-dimensional space.

```
Vector v ∈ ℝⁿ :  v = [v₁, v₂, ..., vₙ]
```

**Norms** measure the "size" of a vector:

| Norm | Name | Formula | Geometric Meaning |
|:----:|:-----|:-------:|:-------------------|
| **L1** | Manhattan Norm | ‖x‖₁ = Σ\|xᵢ\| | Grid-style distance from the origin |
| **L2** | Euclidean Norm | ‖x‖₂ = √(Σxᵢ²) | Straight-line distance from the origin |

> 📌 *In this project:* L1 norm drives Lasso regularization (produces sparse weights); L2 norm drives Ridge regularization and underlies distance-based methods like k-NN and k-Means.

<br/>
</details>

<details>
<summary><b>2️⃣ Dot Product</b> — The scalar that measures alignment</summary>

<br/>

```
A · B  =  Σ AᵢBᵢ  =  ‖A‖ ‖B‖ cos(θ)
```

**Properties:**
- Result is always a **scalar**
- A · B = 0 &nbsp;→&nbsp; A ⊥ B (vectors are orthogonal)
- A · B > 0 &nbsp;→&nbsp; vectors point in similar directions
- A · B < 0 &nbsp;→&nbsp; vectors point in opposite directions

> 📌 *In this project:* Cosine similarity (used in recommendation engines & NLP embeddings) is derived directly from the dot product. It's also the core operation behind every neuron's weighted sum in a neural network.

<br/>
</details>

<details>
<summary><b>3️⃣ Cross Product</b> — Finding the perpendicular direction</summary>

<br/>

```
A × B  =  ‖A‖ ‖B‖ sin(θ) n̂
```

**Properties:**
- Defined only in **3D space**
- Result is a vector **perpendicular** to both A and B
- Its magnitude equals the area of the parallelogram spanned by A and B

> 📌 *In this project:* Computing surface normals in 3D graphics, robotics kinematics, and torque calculations in physics simulations.

<br/>
</details>

<details>
<summary><b>4️⃣ Vector Projection</b> — Decomposing one vector along another</summary>

<br/>

```
proj_B(A)  =  (A · B / ‖B‖²) · B
```

**Properties:**
- Splits A into a component **parallel** to B and a component **orthogonal** to B
- The orthogonal component is the "residual" or error term

> 📌 *In this project:* The geometric foundation of least-squares regression and the Gram-Schmidt process used to orthogonalize feature sets.

<br/>
</details>

<details>
<summary><b>5️⃣ Matrix Operations</b> — Addition, multiplication & transpose</summary>

<br/>

A **matrix** is a rectangular array of numbers, often used to represent a dataset (rows = samples, columns = features).

| Operation | Rule | Notes |
|:----------|:-----|:------|
| **Addition** | (A+B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ | Matrices must have identical dimensions |
| **Multiplication** | (AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ | Columns of A must equal rows of B |
| **Transpose** | (Aᵗ)ᵢⱼ = Aⱼᵢ | Rows and columns are swapped |

> 📌 *In this project:* Matrix multiplication is the core operation in every neural network layer (X·W + b). Transposes are used constantly when reshaping data for batch operations and gradient computations.

<br/>
</details>

<details>
<summary><b>6️⃣ Inverse & Determinant</b> — Reversing a transformation</summary>

<br/>

```
A · A⁻¹  =  I        (Identity Matrix)
```

**Properties:**
- Only **square, non-singular** matrices (det ≠ 0) have an inverse
- det(A) = 0 &nbsp;→&nbsp; matrix is **singular** → no unique solution to Ax = b
- |det(A)| represents how much A scales area/volume under transformation

> 📌 *In this project:* Solving linear systems (Ax = b → x = A⁻¹b), checking if a transformation is reversible, and computing the Mahalanobis distance via the inverse covariance matrix.

<br/>
</details>

<details>
<summary><b>7️⃣ Geometric Subspaces</b> — Lines, Planes & Hyperplanes</summary>

<br/>

| Concept | Dimensionality | Description | Application |
|:--------|:---------------:|:-------------|:-------------|
| **Line** | 1D | A 1D subspace | Simple linear regression |
| **Plane** | 2D | A 2D subspace | Decision boundary with 3 features |
| **Hyperplane** | n − 1 | Subspace one dimension less than its ambient space | Decision boundary for SVM / logistic regression in ℝⁿ |

> 📌 *In this project:* Almost every linear classifier (SVM, logistic regression, perceptron) works by finding the hyperplane that best separates classes in feature space.

<br/>
</details>

<details>
<summary><b>8️⃣ Eigenvalues & Eigenvectors</b> — The DNA of a transformation</summary>

<br/>

```
A v  =  λ v
```

| Term | Meaning |
|:-----|:--------|
| **v** (eigenvector) | A direction left **unchanged** by transformation A |
| **λ** (eigenvalue) | The factor by which v is **scaled** |

> 📌 *In this project:* PCA's principal components are the eigenvectors of the data's covariance matrix, and the corresponding eigenvalues represent how much variance each component explains.

<br/>
</details>

<details>
<summary><b>9️⃣ LU Decomposition</b> — Splitting a matrix for faster solving</summary>

<br/>

```
A  =  L · U
```

| Term | Meaning |
|:-----|:--------|
| **L** | Lower triangular matrix |
| **U** | Upper triangular matrix |

> 📌 *In this project:* Speeds up repeatedly solving Ax = b for different b vectors, and is used internally by numerical libraries to compute determinants and inverses efficiently.

<br/>
</details>

<details>
<summary><b>🔟 Singular Value Decomposition (SVD)</b> — The universal decomposition</summary>

<br/>

```
A  =  U Σ Vᵗ
```

| Term | Meaning |
|:-----|:--------|
| **U, V** | Orthogonal matrices (rotations) |
| **Σ** | Diagonal matrix of singular values (scaling factors) |

**Properties:**
- Works for **any** m × n matrix — not just square ones
- Singular values in Σ are ordered from largest to smallest, capturing the most "important" directions first

> 📌 *In this project:* Image compression, noise reduction, recommendation systems (latent factor models), and computing the Moore-Penrose pseudo-inverse.

<br/>
</details>

<details>
<summary><b>1️⃣1️⃣ Dimensionality Reduction</b> — PCA & LDA</summary>

<br/>

| Technique | Type | Goal | Output |
|:----------|:-----|:-----|:-------|
| **PCA** (Principal Component Analysis) | Unsupervised | Maximize variance captured | Orthogonal principal components |
| **LDA** (Linear Discriminant Analysis) | Supervised | Maximize class separability | Discriminant axes that best separate classes |

> 📌 *In this project:* PCA is used for visualization, noise reduction, and feature compression before modeling. LDA is often used as a supervised preprocessing step ahead of classification.

<br/>
</details>

---

## ✅ Topics Covered

- [x] 🧭 Vectors & vector norms (L1, L2)
- [x] ➕ Dot product & geometric interpretation
- [x] ➗ Cross product (3D space)
- [x] 📐 Vector projection
- [x] 🔲 Matrix addition, multiplication & transpose
- [x] 🔄 Matrix inverse & determinant
- [x] 🌐 Lines, planes & hyperplanes
- [x] 🧩 Eigenvalues & eigenvectors
- [x] 🧮 LU decomposition
- [x] 📉 Singular Value Decomposition (SVD)
- [x] 🎯 PCA & LDA for dimensionality reduction

---

## 🧠 Key Takeaways

| Concept | Core Formula | Why It Matters |
|---|---|---|
| 🧭 Norms | ‖x‖₁, ‖x‖₂ | Foundation for regularization & distance metrics |
| ➕ Dot Product | A·B = ‖A‖‖B‖cos(θ) | Measures similarity / alignment between vectors |
| ➗ Cross Product | A × B | Produces a vector perpendicular to both inputs (3D) |
| 📐 Projection | proj_B(A) | Basis of least-squares regression & orthogonalization |
| 🔲 Matrix Ops | AB, Aᵗ | Core of neural network computations |
| 🔄 Inverse / Det | A⁻¹, det(A) | Solves linear systems; checks invertibility |
| 🌐 Hyperplanes | ℝⁿ⁻¹ | Defines decision boundaries for classifiers |
| 🧩 Eigen Decomposition | Av = λv | Powers PCA & spectral methods |
| 🧮 LU Decomposition | A = LU | Enables efficient system solving |
| 📉 SVD | A = UΣVᵗ | Universal factorization for any matrix |
| 🎯 PCA / LDA | Eigen-based projections | Reduces dimensionality while preserving information |

---

## 🚀 How to Use This Guide

### 📋 Prerequisites

```bash
# No installation required — this is a theory reference!
# Optional: experiment with the formulas hands-on
pip install numpy scipy matplotlib
```

### 🛠️ Step-by-Step

**Step 1 — Start with the basics**
```
Read Section 1 → 4 (Vectors, Norms, Dot/Cross Product, Projection)
```

**Step 2 — Move on to Matrices**
```
Read Section 5 → 6 (Matrix Operations, Inverse & Determinant)
```

**Step 3 — Build geometric intuition**
```
Read Section 7 (Lines, Planes, Hyperplanes)
```

**Step 4 — Tackle the decompositions**
```
Read Section 8 → 10 (Eigen Decomposition, LU, SVD)
```

**Step 5 — Apply it all**
```
Read Section 11 (PCA & LDA) and revisit the Quick Reference for revision
```

> 💡 Each section's **"In this project"** note shows exactly where the concept is applied in practice.

---

## 📁 File Structure

```
📦 calculative-foundation/
│
├── 📄 theory_concepts.md              ← This file (Linear Algebra Theory)
├── 📓 notebooks/
│   └── linear_algebra_practice.ipynb  ← Hands-on examples for each concept
├── 📊 datasets/
│   └── sample_data.csv                ← Sample data for practice
└── 🧮 src/
    └── linear_algebra_utils.py        ← Reusable helper functions
```

---

## 🧠 Key Concepts Quick Reference

```
📌 Vector              →  Ordered list of numbers; has magnitude & direction
📌 L1 / L2 Norm        →  Manhattan / Euclidean "size" of a vector
📌 Dot Product         →  Σ AᵢBᵢ = ‖A‖‖B‖cos(θ) — scalar similarity measure
📌 Cross Product       →  3D-only; produces a vector ⊥ to both inputs
📌 Projection          →  Component of A that lies along direction B
📌 Matrix Multiply     →  (AB)ᵢⱼ = Σₖ AᵢₖBₖⱼ — combines two matrices
📌 Transpose           →  Swap rows and columns: (Aᵗ)ᵢⱼ = Aⱼᵢ
📌 Inverse             →  A⁻¹ such that A·A⁻¹ = I (square, non-singular only)
📌 Determinant         →  Scalar encoding invertibility & scaling factor
📌 Hyperplane          →  (n−1)-dimensional decision boundary in ℝⁿ
📌 Eigenvector/value   →  Av = λv — direction & scale of a transformation
📌 LU Decomposition    →  A = LU — fast solving of Ax = b
📌 SVD                 →  A = UΣVᵗ — works for any m × n matrix
📌 PCA                 →  Unsupervised; maximizes variance; uses covariance eigenvectors
📌 LDA                 →  Supervised; maximizes class separability
```

---

## 📌 Assumptions & Scope

1. This document covers **theory only** — no dataset-specific computations are included
2. All vectors are assumed to be **column vectors** unless stated otherwise
3. Matrix dimensions are assumed **compatible** for the operations described
4. A **"square matrix"** has equal row/column counts; **"non-singular"** means det ≠ 0
5. Geometric intuition is illustrated using ℝ² / ℝ³; concepts generalize to ℝⁿ
6. Symbols: `ᵗ`/`ᵀ` = transpose, `⁻¹` = inverse, `λ`/`v` = eigenvalue/eigenvector, `Σ` = singular value matrix

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" width="100%"/>

**Made with ❤️ by [Meet Gajera](https://github.com/meet6949)**

*Calculative Foundation — Where Every Equation Finds Its Meaning*

⭐ *If this guide helped you, consider giving it a star!* ⭐

</div>
