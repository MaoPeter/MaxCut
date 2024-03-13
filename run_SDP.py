import weight_matrix_constructor
import SDP
import cut_value

matrix_type = "Cycle"
n = 150
weightArr = weight_matrix_constructor.makeWeightArray(matrix_type, n)
partition, cut, SDPval = SDP.maxCutGoemansWilliamson(n, weightArr)
print(partition)
print(cut)
print(SDPval)