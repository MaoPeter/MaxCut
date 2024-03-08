import sys
import weight_matrix_constructor
import SDP
import rayleigh_approach
import cut_value

if len(sys.argv) <= 2:
    print("Arguments needed for size of graph and search mode respectively")
else:
    n = int(sys.argv[1])
    mode = int(sys.argv[2])
    if mode == 1: #default random generation comparing SDP to rayleigh_approach
        tied_graphs = []
        SDP_favored_graphs = []
        rayleigh_favored_graphs = []
        rayleigh_perturbed_graphs = []
        for i in range(int(10000 / n)):
            W = weight_matrix_constructor.makeWeightArray("Random", n)
            SDP_partition, SDP_cut = SDP.maxCutGoemansWilliamson(n, W)
            rayleigh_partition, rayleigh_cut = rayleigh_approach.maxCutRayleigh(W)
            rayleigh_perturbed_partition, rayleigh_perturbed_cut = rayleigh_approach.maxCutRayleighPerturbed(W)
            if SDP_cut > rayleigh_cut and SDP_cut > rayleigh_perturbed_cut:
                SDP_favored_graphs += [W]
            elif rayleigh_cut > SDP_cut and rayleigh_cut > rayleigh_perturbed_cut:
                rayleigh_favored_graphs += [W]
            elif rayleigh_perturbed_cut > SDP_cut and rayleigh_perturbed_cut > rayleigh_cut:
                rayleigh_perturbed_graphs += [W]
            else:
                tied_graphs += [W]
        print("Number of tied graphs: ", len(tied_graphs))
        print("Number of SDP favored graphs: ", len(SDP_favored_graphs))
        print("Number of Rayleigh favored graphs: ", len(rayleigh_favored_graphs))
        print("Number of Perturbed Rayleigh favored graphs: ", len(rayleigh_perturbed_graphs))