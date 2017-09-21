from collections import Counter
numShoes = int(input())
shoeSize = Counter(map(int, input().split()))
numCustomers = int(input())
money = []

for x in range (numCustomers):
    cust = list(map(int,input().split()))
    if shoeSize[cust[0]] > 0:
        money.append(cust[1])
        shoeSize[cust[0]] -= 1

print (sum(money))
