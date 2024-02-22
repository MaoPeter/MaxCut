import itertools

# Calculate the value of a cut for a given weight matrix and partition
# Note that partition is an array of 1's and -1's and each entry corresponds to a vertex
def cutValue(W, partition):
    return sum([W[i][j] if partition[i]*partition[j] == -1 else 0 for i,j in itertools.product(range(len(partition)),range(len(partition)))])