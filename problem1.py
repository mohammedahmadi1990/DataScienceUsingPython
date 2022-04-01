import numpy as np

# #################### Problem 1 ##########################

def ref(A):
    R = A
    num_row = len(R)
    num_col = len(R[0])
    row_idx = 0
    pvt_idx = 0
    pvt_idx_list = []
    eps = pow(10,-10)
    while (row_idx < num_row and pvt_idx < num_col):
        temp = [R[i][pvt_idx] for i in range(row_idx,num_row)]
        if checkAllZero(temp, eps):
            pvt_idx += 1
            continue
        if np.abs(R[row_idx][pvt_idx]) <= eps:
            temp2 = [R[j][pvt_idx] for j in range(row_idx,num_row)]
            nonzero_idx = np.argmax(temp2) # - eps)
            R[row_idx][:] = R[row_idx + nonzero_idx][:]
        for r in range(row_idx + 1, num_row):
            multiplier = np.multiply(-1,R[r][pvt_idx])/R[row_idx][pvt_idx]
            R[r][:] += np.multiply(multiplier, R[row_idx][:])
        pvt_idx_list.append(pvt_idx)
        pvt_idx += 1
        row_idx += 1
    return R, pvt_idx_list

def rref(A):
    R,pvt_idx_list = ref(A)
    num_row = len(R)
    num_col = len(R[0])
    for row_idx, pvt_idx in enumerate(pvt_idx_list):
        for i in range(0, row_idx):
            multiplier = np.multiply(-1,R[i][pvt_idx])/R[row_idx][pvt_idx]
            R[i][:] += np.multiply(multiplier, R[row_idx][:])
    for row_idx, pvt_idx in enumerate(pvt_idx_list):
        R[row_idx][:] = np.divide(R[row_idx][:],R[row_idx][pvt_idx])
    return R


def checkAllZero(list1, val):
    for x in list1:
        if np.abs(x) > val:
            return False
    return True

def printMatrix(mat):
    for line in mat:
        print('  '.join(map(str, line)))


# ### RUN SAMPLE ####
# array1 = [[1,2,2,1], [4,8,9,3], [0,3,2,1]]
# array2 = [[1,2,3], [2,4,6], [1,4,8]]
#
# print("\nInput: ")
# inputMatrix = array1
# printMatrix(inputMatrix)
#
# print("\nREF: ")
# r01,idx = ref(inputMatrix)
# printMatrix(r01)
# print("\nRREF: ")
# r02 = rref(inputMatrix)
# printMatrix(r02)

