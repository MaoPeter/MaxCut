import numpy as np
import cvxpy as cp
import cut_value

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
    
    # pick 10 random planes in R^n
    # r = np.random.normal(0,1,n)
    # r = r / np.linalg.norm(r)
    # separation = U @ r
    # partition = [1 if separation[i] >= 0 else -1 for i in range(n)]
    r = np.random.normal(0,1,n)
    r = r / np.linalg.norm(r)
    separation = U @ r
    best_partition = [1 if separation[i] >= 0 else -1 for i in range(n)]
    best_cut = cut_value.cutValue(W, best_partition)
    for i in range(10):
        r = np.random.normal(0,1,n)
        r = r / np.linalg.norm(r)
        separation = U @ r
        partition = [1 if separation[i] >= 0 else -1 for i in range(n)]
        latest_cut = cut_value.cutValue(W, partition)
        if latest_cut > best_cut:
            best_partition = partition
            best_cut = latest_cut
    return (best_partition, latest_cut, problem.value)