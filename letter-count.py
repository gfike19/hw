fil = open("Latin-Lipsum.txt", "r")
txt = ""
for line in fil:
    txt += line
lst = txt.split()
dic = {}
for each in lst:
    allkeys = dic.keys()
    if each not in allkeys:
        dic[each] = 1
    else:
        val = dic[each] + 1
        dic[each] = val

allkeys = list(dic.keys())
allkeys.sort()
newDic = {}
for each in allkeys:
    newDic[each] = dic[each]

for k,v in newDic.items():
    print(k,v)
