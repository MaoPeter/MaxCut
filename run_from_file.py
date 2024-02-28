import sys
import weight_matrix_constructor
import SDP
import cut_value

file = sys.argv[1]

weightArr = weight_matrix_constructor.makeWeightArray("File", filename=file)
n = len(weightArr)
partition = SDP.maxCutGoemansWilliamson(n, weightArr)
print(partition)
cut = cut_value.cutValue(weightArr, partition)
print(cut)