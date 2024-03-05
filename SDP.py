import numpy as np
import cvxpy as cp

def maxCutGoemansWilliamson(n, weightArray):
    W = np.array(weightArray) # convert the array to a numpy array

    # solve the SDP
    X = cp.Variable((n, n), PSD=True)
    constraints = [X[i][i] == 1 for i in range(n)]
    objective = cp.Minimize(cp.trace(W@X)/2)
    problem = cp.Problem(objective, constraints)
    problem.solve()

    # factorize the solution into X = UU^T
    eigenvalues, eigenvectors = np.linalg.eigh(X.value)
    # take the absolute values to make all fp error zeros into positive.
    U = eigenvectors @ np.diagflat(np.sqrt(np.abs(eigenvalues))) 
    
    # pick random plane in R^n
    r = np.random.normal(0,1,n)
    r = r / np.linalg.norm(r)
    separation = U @ r
    partition = [1 if separation[i] >= 0 else -1 for i in range(n)]
    return partition