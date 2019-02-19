data = open("data0.txt", "r")
text = []
for line in data:
    text.append(line)
data.close()
for line in text:
    temp = line.strip("\n")
    temp = temp.split(" ")
    name = temp[0]
    hrs = int(temp[1])
    rate = float(temp[2])
    pay = float(rate * hrs)
    print(name, hrs, pay)