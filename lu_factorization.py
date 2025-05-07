""""
Gaussian Elimination Cost Analysis and Comparison to Inverse Matrix Approach
""""

# Assume an n x n matrix M to solve Ax = b via Gaussian Elimination
# We analyze the algorithm's time complexity using pseudocode structure.

""""
Step 1: Gaussian Elimination (LU Decomposition without pivoting)
We eliminate entries below the diagonal by performing row operations.
Each operation consists of:
  - computing a multiplier l_ij = m_ij / m_jj
  - updating row i: row_i = row_i - l_ij * row_j
This results in an upper triangular matrix.
""""

def gaussian_elimination_cost(n):
    cost = 0
    for j in range(1, n + 1):
        for i in range(j + 1, n + 1):
            # Compute l_ij and perform row subtraction (each is O(n) work)
            cost += n
    return cost

""""
Step 2: Total Cost
There are ~n^2/2 such row updates, each costing O(n)
=> Total cost is O(n^3)
""""
n = 100  # Example size
print("Gaussian Elimination estimated operations:", gaussian_elimination_cost(n))

""""
Step 3: Matrix Inversion Cost
To solve Ax = b using A^{-1}:
  - Compute A^{-1} (costs O(n^3))
  - Multiply A^{-1} * b (costs O(n^2))

Total cost = O(n^3 + n^2) = O(n^3)
But this is wasteful if you only need a solution to Ax = b.
""""
def inverse_method_cost(n):
    inversion = n ** 3      # Inverting matrix
    multiplication = n ** 2 # Multiply with b
    return inversion + multiplication

print("Inverse Method estimated operations:", inverse_method_cost(n))

""""
Conclusion:
Both methods are O(n^3), but:
- Gaussian Elimination is **direct** and avoids computing the full inverse
- Matrix Inversion does **extra unnecessary work** unless you need the full inverse

=> Gaussian Elimination is more efficient for solving Ax = b.
""""
