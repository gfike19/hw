# print("Exercise 1")
# oldText = input("Enter some text: ")
# dist = int(input("Enter rotation value: "))
#
# newText = ""
# for each in oldText:
#     oldValue = ord(each)
#     newValue = (oldValue + dist) % 127
#     newChar = chr(newValue)
#     newText += newChar
# print(newText)
#
# print("\n")
# print("Exercise 2")
# oldText = input("Enter encrypted text: ")
# dist = int(input("Enter rotation value: "))
# newText = ""
# for each in oldText:
#     oldValue = ord(each)
#     newValue = (oldValue - dist) % 127
#     newChar = chr(newValue)
#     newText += newChar
# print(newText)
#
# print("\n")
# print("Exercise 3")
# oldFileName = input("Enter the input filename: ")
# oldFile = open(oldFileName, "r")
# newFileName = input("Enter the output filename: ") + ".txt"
# dist = int(input("Enter rotation value: "))
# oldText = ""
# for each in oldFile:
#     oldText += each
# oldFile.close()
# newText = ""
# for each in oldText:
#     oldValue = ord(each)
#     newValue = (oldValue - dist) % 127
#     newChar = chr(newValue)
#     newText += newChar
# newFile = open(newFileName, "w+")
# for each in newText:
#     newFile.write(each)
# newFile.close()
#
# print("\n")
# print("Exercise 4")
# decimal = int(input("Enter a decimal integer: "))
# if decimal == 0:
#     print(0)
# else:
#     print("Quotient Remainder Octal")
#     bstring = ""
#     while decimal > 0:
#         remainder = decimal % 8
#         decimal = decimal // 8
#         ostring = str(remainder) + bstring
#         print("%5d%8d%12s" % (decimal, remainder, ostring))
#     print("The octal representation is", ostring)
#
# ostring = input("Enter a string of octal digits: ")
# decimal = 0
# exponent = len(ostring) - 1
# for digit in ostring:
#     decimal = decimal + int(digit) * 8 ** exponent
#     exponent = exponent - 1
# print("The integer value is", decimal)
#
# print("\n")
# print("Exercise 5")
#
# print("\n")
# print("Exercise 6")
#
# print("\n")
# print("Exercise 7")
#
# print("\n")
# print("Exercise 8")
# oldFileName = input("Enter the input file name: ")
# newFileName = input("Enter the output file name: ")
# oldFile = open(oldFileName, "r")
# text = ""
# for line in oldFile:
#     text += line
# oldFile.close()
# newFile = open(newFileName, "w+")
# for each in text:
#     newFile.write(each)
# newFile.close()
#
# print("\n")
# print("Exercise 9")
# oldFileName = input("Enter the input file name: ")
# newFileName = input("Enter the output file name: ")
# oldFile = open(oldFileName, "r")
# text = ""
# for line in oldFile:
#     text += line
# oldFile.close()
# newFile = open(newFileName, "w+")
# counter = 0
# for each in text:
#     newLine = str(counter) + ">" + each
#     newFile.write(newLine)
# newFile.close()
#
# print("\n")
# print("Exercise 10")
# fileOneName = input("Enter the input file name: ")
# fileTwoName = input("Enter the output file name: ")
# fileOneText = ""
# fileTwoText = ""
# fileOne = open(fileOneName, "r")
# for each in fileOne:
#     fileOneText += each
# fileOne.close()
# fileTwo = open(fileTwoName, "r")
# for each in fileTwo:
#     fileTwoText += each
# fileTwo.close()
#
# counter = 0
# for each in fileOneText:
#     if each != fileTwoText[counter]:
#         print("No " + each)
#         break
#     else:
#         counter += 1
# print("Yes")

# Exercise 12
fileName = input("Enter the file name: ")
data = open(fileName, "r")
text = []
for each in data:
    text.append(each.split(" "))
data.close()
for line in text:
    wages = float(line[1])
    hrs = float(line[2])
    name = line[0]
    pay = float(wages) * float(hrs)
    print(name, hrs, pay)
