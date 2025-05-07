# Minimization in Applied Linear Algebra: Comprehensive Study Guide

## Theoretical Foundations

### Minimization Principles in Physical & Mathematical Systems  
Many physical and mathematical systems operate on principles of minimization. In physics, stable equilibrium corresponds to minimizing potential energy. In mathematics, solving equations can be cast as minimization: a system  
```
f_1(x)=0, …, f_m(x)=0
```  
can be reformulated by minimizing  
```
p(x)=f_1(x)^2 + … + f_m(x)^2 = ||f(x)||^2.
```  
The minimum value `p(x*)=0` is attained exactly when `x*` solves all equations. Thus, minimization provides a unifying framework for finding optimal or approximate solutions.

### Quadratic Minimization (Single-Variable & Multi-Variable)

**Single-Variable Case:**  
A quadratic function in one variable is  
```
p(x) = a x^2 + 2b x + c.
```  
- If `a>0`, the parabola opens upward and has a unique minimum at  
  ```
  x* = -b/a
  ```  
  with minimum value  
  ```
  p(x*) = c - b^2/a.
  ```  
- If `a<0`, it opens downward and is unbounded below (no finite minimum).  
- If `a=0`, the function is linear (no bounded minimum unless constant).

**Multi-Variable Case:**  
A quadratic function in R^n can be written

```
p(x) = x^T K x - 2 x^T f + c,
```

where `K` is an n×n symmetric matrix, `f` is a constant vector, and `c` is a constant scalar.  
To minimize, set the gradient to zero:

```
∇p(x) = 2Kx - 2f = 0 ⇒ Kx = f.
```

If `K` is invertible (positive definite), the unique minimizer is

```
x* = K^{-1} f,
```

and the minimum value is

```
p(x*) = c - f^T K^{-1} f.
```

### Least Squares Minimization and Geometric Interpretation  
Given an (often overdetermined) linear system `Ax = b` where `A` is m×n, we define the residual `r = b - Ax` and minimize the squared error

```
p(x) = ||Ax - b||^2.
```

The vector `x*` minimizing this is called the **least squares solution**. Geometrically, the set `{Ax : x in R^n}` is a subspace of R^m. Finding `x*` projects `b` orthogonally onto that subspace. The residual `b - Ax*` is orthogonal to every column of `A`.

### Positive Definite vs. Semi-Definite Matrices (Uniqueness of Minima)  
- **Positive Definite (PD):** If `K` is PD (`x^T K x > 0` for all nonzero `x`), then `p(x)` is strictly convex and has a unique global minimizer `x* = K^{-1} f`.  
- **Positive Semi-Definite (PSD):** If `K` is PSD (`x^T K x ≥ 0`), minima exist but may not be unique. Any component in the nullspace of `K` can be added to a minimizer without changing the value.  
- **Indefinite:** If `K` has negative eigenvalues, `p(x)` is unbounded below and has no global minimum.

For least squares, `K = A^T A` is always PSD. If `A` has full column rank, `A^T A` is PD and the least squares solution is unique. If `A` is rank-deficient, infinitely many minimizers exist (all yielding the same minimal error).

### Normal Equations and Conditions for Solvability  
Setting the gradient of `||Ax - b||^2` to zero yields the **normal equations**:

```
A^T A x = A^T b.
```

- If `A^T A` is invertible (full column rank), the unique solution is

  ```
  x* = (A^T A)^{-1} A^T b.
  ```

- If `A^T A` is singular, there are infinitely many solutions minimizing the error. One often selects the minimum-norm solution via the pseudoinverse.

**Weighted Least Squares:** Introduce a positive-definite weight matrix `C`. Minimize `||C^{1/2}(Ax - b)||^2`, leading to

```
A^T C A x = A^T C b,
x* = (A^T C A)^{-1} A^T C b.
```

Weights adjust for varying reliability or importance of different equations or data points.

---

## Problem-Solving Strategies

1. **Solve Least Squares via Normal Equations**  
   - Form `A^T A` and `A^T b`.  
   - Solve `A^T A x = A^T b`.  
   - If `A^T A` is invertible, compute `x* = (A^T A)^{-1} A^T b`.

2. **Quadratic Forms (Matrix Method)**  
   - Write `p(x) = x^T K x - 2 x^T f + c`.  
   - Identify `K` (symmetric), `f`, and `c`.  
   - Solve `Kx = f`.  
   - If `K` is PD, this yields the unique minimizer `x*`.

3. **Closest Point Problems via Gram Matrix**  
   - Given basis `{w_i}` for subspace `W`, form Gram matrix `K_{ij} = <w_i, w_j>`.  
   - Compute `f_i = <w_i, b>`.  
   - Solve `Kx = f` to get coefficients `x`.  
   - Reconstruct projection `w* = sum_i x_i w_i`.

4. **Gradient Descent vs. Analytical Minimization**  
   - Analytical methods (normal equations, direct inversion) give closed‑form solutions for linear quadratics.  
   - Gradient descent iteratively updates `x_{t+1} = x_t - α ∇p(x_t)` and is used when analytical solutions are infeasible (e.g., complex/non-quadratic loss, large-scale).

---

## Worked Examples

### Example 1: Quadratic Function Minimization  
**Problem:** Minimize  
```
p(x_1,x_2) = 4x_1^2 - 2x_1x_2 + 3x_2^2 + 3x_1 - 2x_2 + 1.
```  
**Solution:**  
1. Identify `K = [[4, -1], [-1, 3]]`, `f = [-3/2, 1]^T`, `c=1`.  
2. Solve `Kx=f` to get `x* = [-7/22, 5/22]^T`.  
3. Since `K` is PD, this is unique. Minimum `p(x*) = 13/44`.

---

### Example 2: Least Squares for Overdetermined System  
**Problem:**  
```
A = [[1,2],[3,-1],[-1,2],[1,-1],[2,1]], b = [1,0,-1,2,2]^T.
```  
**Solution:**  
1. Compute `A^T A = [[16,-2],[-2,11]]`.  
2. Compute `A^T b = [8,0]^T`.  
3. Solve `(A^T A)x = A^T b`: `x* ≈ [0.5116, 0.0930]^T`.  
4. Min squared error `||Ax*-b||^2 ≈ 4.369`.

---

### Example 3: Closest Point in a Plane  
**Problem:**  
```
w1 = [1,2,-1]^T, w2 = [2,-3,-1]^T, b = [1,0,0]^T.
```  
**Solution:**  
1. Gram `K = [[6,-3],[-3,14]]`.  
2. `f = [1,2]^T`.  
3. Solve `Kx=f`: `x* = [4/15,1/5]`.  
4. Projection `w* ≈ [0.667,-0.067,-0.467]^T`.  
5. Distance `||b-w*|| ≈ 0.5774`.

---

## Applications of Minimization

- **Regression & Data Fitting**: Least squares determines best-fit parameters for models.  
- **Classification**: k-NN, SVM involve distance or quadratic minimization.  
- **Control & Robotics**: Kalman filters, path planning minimize cost/estimation error.  
- **Physics & Engineering**: Finite element methods minimize energy functionals.  
- **Machine Learning**: Training models minimize loss functions analytically or by gradient descent.

---

## Summary Tables

**Key Formulas**  
| Type                 | Equation                | Solution                       |
| -------------------- | ----------------------- | ------------------------------ |
| Single-var quadratic | `p'(x)=0`               | `x*=-b/a`, `p(x*)=c-b^2/a`     |
| Multi-var quadratic  | `Kx=f`                  | `x*=K^{-1}f`; min `c-f^T K^{-1}f` |
| Least squares        | `A^T A x = A^T b`       | `x*=(A^T A)^{-1}A^T b`         |
| Weighted LS          | `A^T C A x = A^T C b`   | `x*=(A^T C A)^{-1}A^T C b`     |
| Orthonormal proj.    | `w* = sum <b,u_i> u_i`  | Direct inner products         |

**Conditions**  
- Unique if matrix PD.  
- Multiple if PSD but singular.  
- None if indefinite.
