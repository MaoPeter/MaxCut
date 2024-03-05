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
partition = SDP.maxCutGoemansWilliamson(n, weightArr)
print(partition)
cut = cut_value.cutValue(weightArr, partition)
print(cut)