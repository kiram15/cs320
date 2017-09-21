from collections import OrderedDict
oDict = OrderedDict()
nameList = []

for x in range(int(input())):
    name, price = input().rsplit(' ',1)
    if name not in nameList:
        oDict[name] = price
        
    else:
        newNum = int(oDict[name]) + int(price)
        oDict[name] = newNum    
    nameList.append(name)

for k, v in oDict.items():
    print (k, v)
