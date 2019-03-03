print("Exercise 2")

fileName = input("Enter the input file name: ")
fil = open(fileName, "r")
lst = []
for line in fil:
    lst.append(line)
sz = len(lst)
print("The file has", sz, "lines. ")
choice = None
while choice != 0:
    choice = int(input("Enter a line number [0 to quit]: "))
    print(choice, ":", lst[choice])
    choice = int(input("Enter a line number [0 to quit]: "))


print("\n")
print("Exercise 7")
fileName = input("Enter the input file name: ")
fil = open(fileName, "r")
txt = ""
for line in fil:
    txt += line
lst = txt.split()
lst.sort()
for each in lst:
    print(each)

print("\n")
print("Exercise 8")
fileName = input("Enter the input file name: ")
fil = open(fileName, "r")
txt = ""
for line in fil:
    txt += line
lst = txt.split()
dict = {}
for k,v in dict.items():
    if k not in dict.keys():
        dict[k] = 0
    else:
        val = dict[k]
        dict[k] = val + 1
for k, v in dict.items():
    print(k, v)
