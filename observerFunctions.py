
# inputData     : [num_of_states + 1 x 1] input data vector starting with time sample at first element

import numpy as np

def  kalmanFilterFun(inputData):

    outputData = np.zeros(np.shape(inputData))

    outputData[0] = inputData[0]
    outputData[1] = inputData[1]
    outputData[2] = inputData[2]

    return outputData

