# Rotate an array in left 
# Required Parameters
# Rotations = 2
# arrzy elements = [1,2,3,4,5,6]
#

import array

arr = array.array("i",[1,2,3,4,5,6])
arrSize = len(arr)
   
def printArray(arr,arrSize):
    for i in range(arrSize):
        print(arr[i])
        
def leftRotate(arr,rotations,arrSize):
    for i in range(rotations):
        leftRotateByOne(arr,arrSize)

def leftRotateByOne(arr,arrSize):
    temp = arr[0]
    for i in range(arrSize-1):
        arr[i] = arr[i + 1]
    arr[arrSize-1] = temp

print(" \n BEFORE ROTATE \n ")
printArray( arr, arrSize)

leftRotate(arr,1,arrSize)

print(" \n AFTER ROTATE \n ")

printArray(arr,arrSize)
