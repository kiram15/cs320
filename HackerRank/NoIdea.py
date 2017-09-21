parameters = input()
newArray = input().split()
A = set(input().split())
B = set(input().split())
outcome = 0

for i in newArray:
  if (i in A):
    outcome+=1
  if (i in B):
    outcome-=1
    
print (outcome)
