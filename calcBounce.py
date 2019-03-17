ht = float(input("Enter the height from which the ball is dropped: "))
bounciness = float(input("Enter the bounciness index of the ball: "))
num = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
dist = 0
while num > 0:
    dist += ht
    ht = ht * bounciness
    dist += ht
    num -= 1
print("Distance traveled is", ht)

