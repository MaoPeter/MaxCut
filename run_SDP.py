import weight_matrix_constructor
import SDP
import cut_value

matrix_type = "Complete"
n = 12
weightArr = weight_matrix_constructor.makeWeightArray(matrix_type, n, [])
partition = SDP.maxCutGoemansWilliamson(n, weightArr)
print(partition)
cut = cut_value.cutValue(weightArr, partition)
print(cut)