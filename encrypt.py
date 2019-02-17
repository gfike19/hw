# import os
#
# fileName = input("Enter the name of the file you would like to encriypt: ")
#
# if (os.listdir("C:\\Users\\amfzn\PycharmProjects")):
#     num = int(input("Enter a distance value: "))
#
#
#
#
#     code = ""
#     for ch in allText:
#         ordvalue = ord(ch)
#         cipherValue = ordvalue + distance
#         if cipherValue > 122:
#             cipherValue = ord("a") + (cipherValue - 123)
#             code += chr(cipherValue)
#
#     newFile = (fileName + "-encrupted.txt", "a+")
#     for each in code:
#         newFile.write(each)
