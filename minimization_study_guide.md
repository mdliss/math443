# Minimization in Applied Linear Algebra: Comprehensive Study Guide

## 📚 Theoretical Foundations

### ✅ Minimization Principles in Physical & Mathematical Systems

Many physical and mathematical systems operate on principles of minimization. In physics, stable equilibrium corresponds to minimizing potential energy. In mathematics, solving equations can be cast as minimization: a system  

```
f_1(x) = 0, …, f_m(x) = 0
```

can be reformulated by minimizing:  

```
p(x) = f_1(x)^2 + … + f_m(x)^2 = ||f(x)||^2.
```

The minimum value `p(x*) = 0` is attained exactly when `x*` solves all equations. Thus, minimization provides a unifying framework for finding optimal or approximate solutions.

---

### ✅ Quadratic Minimization (Single-Variable & Multi-Variable)

#### 🔹 Single-Variable Case
A quadratic function in one variable is defined as:  

```
p(x) = a x^2 + 2b x + c
```

- If `a > 0`, the parabola opens upward with a unique minimum at:

```
x* = -b / a
```

with minimum value:  

```
p(x*) = c - b^2 / a
```

- If `a < 0`, the parabola opens downward (no finite minimum).  
- If `a = 0`, the function is linear (no bounded minimum unless constant).

#### 🔹 Multi-Variable Case
A quadratic function in `R^n` can be expressed as:  

```
p(x) = x^T K x - 2 x^T f + c
```

where `K` is an `n x n` symmetric matrix, `f` is a constant vector, and `c` is a constant scalar. To minimize, set the gradient to zero:  

```
∇p(x) = 2Kx - 2f = 0  ⇒  Kx = f
```

If `K` is invertible (positive definite), the unique minimizer is:  

```
x* = K^{-1} f
```

with the minimum value:  

```
p(x*) = c - f^T K^{-1} f
```

---

### ✅ Least Squares Minimization & Geometric Interpretation

Given an overdetermined linear system `Ax = b`, the residual is defined as:

```
r = b - Ax
```

We minimize the squared error:

```
p(x) = ||Ax - b||^2
```

The vector `x*` minimizing this is the **least squares solution**. Geometrically, it projects `b` orthogonally onto the column space of `A`.

---

### ✅ Positive Definite vs. Semi-Definite Matrices

- **Positive Definite (PD):** Unique global minimizer `x* = K^{-1} f`.  
- **Positive Semi-Definite (PSD):** Multiple minimizers; any nullspace component can be added to a minimizer without changing the minimum value.  
- **Indefinite:** Unbounded below, no global minimum.

For least squares, `K = A^T A` is always PSD. If `A` has full column rank, `A^T A` is PD and the least squares solution is unique.

---

### ✅ Normal Equations & Weighted Least Squares

Setting the gradient of `||Ax - b||^2` to zero yields:

```
A^T A x = A^T b
```

- If `A^T A` is invertible:

```
x* = (A^T A)^{-1} A^T b
```

**Weighted Least Squares:**

```
A^T C A x = A^T C b
```

where `C` is a positive-definite weight matrix.

---

## 🛠️ Problem-Solving Strategies

1. **Least Squares via Normal Equations:**
   - Form `A^T A` and `A^T b`.
   - Solve `A^T A x = A^T b`.
   - If `A^T A` is invertible, `x* = (A^T A)^{-1} A^T b`.

2. **Quadratic Forms (Matrix Method):**
   - Identify `K`, `f`, `c` and solve `Kx = f`.

3. **Closest Point via Gram Matrix:**
   - Construct Gram matrix `K_{ij} = <w_i, w_j>`.
   - Solve `Kx = f` to obtain coefficients.

4. **Gradient Descent:**
   - Iteratively update `x_{t+1} = x_t - α ∇p(x_t)`.

---

## ✅ Worked Examples

**Example 1: Quadratic Function Minimization**

```
p(x1, x2) = 4x1^2 - 2x1x2 + 3x2^2 + 3x1 - 2x2 + 1
```

- Identify `K = [[4, -1], [-1, 3]]`, `f = [-3/2, 1]^T`, `c = 1`
- Solve `Kx = f` to obtain `x* = [-7/22, 5/22]^T`
- Since `K` is PD, this is unique. Minimum `p(x*) = 13/44`.

**Example 2: Least Squares for Overdetermined System**

```
A = [[1, 2], [3, -1], [-1, 2], [1, -1], [2, 1]], b = [1, 0, -1, 2, 2]^T
```

- Compute `A^T A` and `A^T b`
- Solve `(A^T A)x = A^T b` to obtain `x* ≈ [0.5116, 0.0930]^T`
- Minimum squared error `||Ax* - b||^2 ≈ 4.369`

---

## ✅ Applications of Minimization

- **Regression:** Least squares for data fitting.  
- **Classification:** Distance-based methods like SVM.  
- **Control Systems:** Kalman filters minimize estimation error.  
- **Physics & Engineering:** Minimizing energy functionals.  
- **Machine Learning:** Gradient descent to minimize loss.

---

## ✅ Summary Table

| Type                 | Equation                | Solution                       |
| -------------------- | ----------------------- | ------------------------------ |
| Single-var quadratic | `p'(x) = 0`             | `x* = -b / a`                  |
| Multi-var quadratic  | `Kx = f`                | `x* = K^{-1} f`                |
| Least squares        | `A^T A x = A^T b`       | `x* = (A^T A)^{-1} A^T b`      |
| Weighted LS          | `A^T C A x = A^T C b`   | `x* = (A^T C A)^{-1} A^T C b`  |

**Conditions:** Unique if matrix is PD; Multiple if PSD; None if indefinite.
