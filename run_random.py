import sys
import weight_matrix_constructor
import SDP
import cut_value

n = 50
if len(sys.argv) > 1:
    seed = int(sys.argv[1])
    weightArr = weight_matrix_constructor.makeWeightArray("Random", n, parameters=[seed])
else:
    weightArr = weight_matrix_constructor.makeWeightArray("Random", n)
partition, cut, SDP_val = SDP.maxCutGoemansWilliamson(n, weightArr)
print(partition)
print(cut)