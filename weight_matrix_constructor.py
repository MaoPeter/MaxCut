# Generate a weight matrix
def makeWeightArray(name, size, parameters=[]):
    W = []
    match name:
        case "Complete":
            W = [[1 for j in range(size)] for i in range(size)]
        case "Cycle":
            W = [[1 if j == (i+1) % size or j == (i-1) % size else 0 for j in range(size)] for i in range(size)]
        case "CompleteBipartite": #where parameters[0] is the largest vertex in the first partition
                                  #and parameters[0]+1 is the smallest vertex in the second partition
            W = [[1 if (j <= parameters[0] and i > parameters[0]) or (j > parameters[0] and i <= parameters[0])
                  else 0 for j in range(size)] for i in range(size)]
        case _:
            return
    return W