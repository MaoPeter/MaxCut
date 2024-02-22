import numpy
import scipy
import cut_value

# Find a cut of a weighted graph (specified by the symmetric matrix W)
# based on rounding the eigenvector associated with the smallest eigenvalue
# of W.

def maxCutRayleigh(W):
    weightArr = numpy.array(W)
    evals_large, evecs_large = scipy.linalg.eigh(weightArr, eigvals=(0,0))
    partition = [1 if evecs_large[i] >= 0 else -1 for i in range(len(evecs_large))]
    return (partition, cut_value.cutValue(W,partition))

def maxCutRayleighPerturbed(W):
    weightArr = numpy.array(W)
    s = weightArr.shape
    noise = numpy.random.normal(0,0.01,s)
    evals_large, evecs_large = scipy.linalg.eigh(weightArr+noise, eigvals=(0,0))
    partition = [1 if evecs_large[i] >= 0 else -1 for i in range(len(evecs_large))]
    return (partition, cut_value.cutValue(W,partition))