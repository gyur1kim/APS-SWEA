newDict = {}
a = 10
b = newDict.get(a, [])
print(b)
b.append(2)
newDict[a] = b
print(newDict)