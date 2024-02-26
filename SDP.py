import numpy as np
import cvxpy as cp
import weight_matrix_constructor as wmc


matrix_type = "Complete"
n = 12

X = cp.Variable((n, n), PSD=True)
W = np.array(wmc.makeWeightArray(matrix_type, n, [4]))


constraints = [X[i][i] == 1 for i in range(n)] 

objective = cp.Minimize(cp.trace(W@X)/2)
problem = cp.Problem(objective, constraints)
problem.solve() #gives negative output
print("status:", problem.status)
print("optimal value", problem.value)
print("optimal var", X.value)

decomposition = numpy.linalg.svd(X.value, full_matrices = True, compute_uv = true, hermitian = True)

#print(W)
#print(W@ np.ones((12, 12)))