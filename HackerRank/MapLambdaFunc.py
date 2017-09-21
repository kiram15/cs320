cube = lambda x: x**3

def fibonacci(n):
    xList = []
    for x in range (1, n+1):
        xList.append(fibHelper(x))   
    return xList
        
def fibHelper(n):
    if(n == 1):
        return 0
    if(n == 2):
        return 1
    else:
        return(fibHelper(n-1) + fibHelper(n-2))
