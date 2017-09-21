def arrays(arr):
    arr=arr[::-1]

    arr=list(map(float,arr))
    arr=numpy.array(arr)    
    return(arr)
    
arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)
