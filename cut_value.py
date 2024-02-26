import itertools

# Calculate the value of a cut for a given weight matrix and partition
# Note that partition is an array of 1's and -1's and each entry corresponds to a vertex
def cutValue(W, partition):
    # Looping over j < i
    return sum([W[i][j] if partition[i]*partition[j] == -1 else 0 for i in range(len(partition)) for j in range(i)])