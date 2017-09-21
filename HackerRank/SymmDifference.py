input()
a = map(int, (input().split()))
set1 = set(a)
input()
b = map(int, (input().split()))
set2 = set(b)

final = sorted(set1 ^ set2)
for i in final:
    print(i)
