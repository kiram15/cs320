if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    secLargest = -101
    Largest = -101
    
    for i in range (0, n):
        if Largest == -101:   # first one
            Largest = arr[i]
        elif Largest < arr[i] and Largest != -101:
            secLargest = Largest
            Largest = arr[i]
        elif secLargest < arr[i] < Largest:
            secLargest = arr[i]
   
    print secLargest
