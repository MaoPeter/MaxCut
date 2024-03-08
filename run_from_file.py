import sys
import weight_matrix_constructor
import SDP
import cut_value

if len(sys.argv) <= 1:
    print("Need file to read for input")
else:
    file = sys.argv[1]

    weightArr = weight_matrix_constructor.makeWeightArray("File", filename=file)
    n = len(weightArr)
    partition, cut = SDP.maxCutGoemansWilliamson(n, weightArr)
    print(partition)
    print(cut)