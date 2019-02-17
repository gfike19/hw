repeat = "y"

while repeat == "y":
    oldText = input("Enter some text: ")
    dist = int(input("Enter rotation value: "))

    newText = ""
    for each in oldText:
        oldValue = ord(each)
        newValue = (oldValue + dist) % 127
        newChar = chr(newValue)
        newText += newChar

    print("New text is", newText)
    repeat = input("Enter some more text? (y/m)")
