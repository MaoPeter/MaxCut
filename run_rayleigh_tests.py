import rayleigh_approach
import weight_matrix_constructor

# Run some tests on the Rayleigh approach

#Try complete bipartite
n,m = 15, 10
W = weight_matrix_constructor.makeWeightArray("CompleteBipartite", n, [m-1])
partition, cut = rayleigh_approach.maxCutRayleigh(W)
print(partition)
print(cut)

#Try the cycle graph
n = 10
W = weight_matrix_constructor.makeWeightArray("Cycle", n)
partition, cut = rayleigh_approach.maxCutRayleigh(W)
print(partition)
print(cut)

#Try the complete graph
n = 10
W = weight_matrix_constructor.makeWeightArray("Complete", n)
partition, cut = rayleigh_approach.maxCutRayleigh(W)
print(partition)
print(cut)

#Try the complete graph with perturbations
n = 10
W = weight_matrix_constructor.makeWeightArray("Complete", n)
partition, cut = rayleigh_approach.maxCutRayleighPerturbed(W)
print(partition)
print(cut)