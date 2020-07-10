import array

def spliFirstHalf(arr, sizeArray, SplitEndPos):
    for j in range(0, SplitEndPos):
        x = arr[0]        
        for i in range(0, sizeArray-1):
            arr[i] = arr[i+1]
        arr[sizeArray-1] = x

arr = [ 1,2 ,3 ,4 ,5 ,6,7,8,9,0]

sizeArray = len(arr)

SplitEndPos = 2

spliFirstHalf(arr, sizeArray, SplitEndPos )

print(" \n AFTER SPLIT ROTATE \n ")

for i in range(sizeArray):
    print(arr[i],"  ")