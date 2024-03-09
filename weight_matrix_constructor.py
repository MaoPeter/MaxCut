import numpy as np

# Generate a weight matrix
def makeWeightArray(name, size=0, *, parameters=[], filename=""):
    W = []
    match name:
        case "Complete":
            W = [[1 if i != j else 0 for j in range(size)] for i in range(size)]
        case "Cycle":
            W = [[1 if j == (i+1) % size or j == (i-1) % size else 0 for j in range(size)] for i in range(size)]
        case "CompleteBipartite": #where parameters[0] is the largest vertex in the first partition
                                  #and parameters[0]+1 is the smallest vertex in the second partition
            W = [[1 if (j <= parameters[0] and i > parameters[0]) or (j > parameters[0] and i <= parameters[0])
                  else 0 for j in range(size)] for i in range(size)]
        case "File":
            data = np.genfromtxt(filename, delimiter=" ", dtype=int)
            s = data[0][0]
            W = [[0 for i in range(s)] for j in range(s)]
            for row in data[1:]:
                W[row[0]-1][row[1]-1] = row[2]
                W[row[1]-1][row[0]-1] = row[2]
        case "Random":
            cutoff = 0.5
            if len(parameters) >= 1:
                np.random.seed(parameters[0])
            if len(parameters) >= 2:
                cutoff = parameters[1]
            W = [[1 if i <= j and np.random.rand() <= cutoff else 0 for i in range(size)] for j in range(size)]
            for j in range(size):
                for i in range(size):
                    if W[i][j] == 0:
                        W[i][j] = W[j][i]
            for i in range(size):
                W[i][i] = 0
        case _:
            return
    return W
