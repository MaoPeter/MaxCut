import rayleigh_approach
import weight_matrix_constructor

# Run some tests on the Rayleigh approach

#Try complete bipartite
print("Bipartite with 15 vertices and split 10,5")
n,m = 15, 10
W = weight_matrix_constructor.makeWeightArray("CompleteBipartite", n, [m-1])
partition, cut = rayleigh_approach.maxCutRayleigh(W)
print(partition)
print(cut)

#Try the cycle graph
print("\nCycle with 10 vertices")
n = 10
W = weight_matrix_constructor.makeWeightArray("Cycle", n)
partition, cut = rayleigh_approach.maxCutRayleigh(W)
print(partition)
print(cut)

#Try the complete graph
print("\nComplete with 10 vertices")
n = 10
W = weight_matrix_constructor.makeWeightArray("Complete", n)
partition, cut = rayleigh_approach.maxCutRayleigh(W)
print(partition)
print(cut)

#Try the complete graph with perturbations
print("\nComplete with 10 vertices using perturbed")
print("(running 10 times)")
cuts = []
for i in range(10):
    n = 10
    W = weight_matrix_constructor.makeWeightArray("Complete", n)
    partition, cut = rayleigh_approach.maxCutRayleighPerturbed(W)
    cuts += [cut]
    print(cut)
print("Average result: " + str(sum(cuts)/len(cuts)))

#Try the complete graph with averaging
print("\nComplete with 10 vertices using averaging")
n = 10
W = weight_matrix_constructor.makeWeightArray("Complete", n)
partition, cut = rayleigh_approach.maxCutRayleighAveraged(W)
print(partition)
print(cut)