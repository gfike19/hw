# import random
print("Exercise 3.2")
s1 = int(input("Enter the first side: "))
s2 = int(input("Enter the second side: "))
s3 = int(input("Enter the third side: "))

if s1**2 + s2**2 == s3**2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
print("\n")

# not solved
# print("Exercise 3.3")
# smaller = int(input("Enter the smaller number: "))
# larger = int(input("Enter the larger number: "))
# myNumber = random.randint(smaller, larger)
# count = 0
# while True:
#     count += 1
#     userNumber = int(input("Enter your guess: "))
#     if userNumber < myNumber:
#         print("Too small")
#     elif userNumber > myNumber:
#         print("Too large")
#     else:
#         print("You've got it in", count, "tries!")
#         break
# print("\n")

print("Exercise 3.4")
ht = int(input("Enter the height from which the ball is dropped: "))
bounciness = float(input("Enter the bounciness index of the ball: "))
num = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
dist = ht
for i in range(num):
    ht = ht * bounciness
    dist = dist + 2 * ht
print("Total distance traveled is: " + dist)
print("\n")

print("Exercise 3.5")
start = int(input("Enter the initial number of organisms: "))
rate = int(input("Enter the rate of growth [a real number > 0]: "))
growTime = int(input("Enter the number of hours to achieve the rate of growth: "))
totalTime = int(input("Enter the total hours of growth: "))
total = start
for i in range(0,totalTime, growTime):
    total = total + rate
print("The total population is " + total)
print("\n")

print("Exercise 3.6")
print("\b")

print("Exercise 3.7")
# slice question?
base = round(float(input("Enter the starting salary: $")), 2)
increase = round(float(input("Enter the annual % increase: ")) / 100, 2)
yrs = int(input("Enter the number of years: "))
header = "Year   Salary"
print(header)
print("-" * len(header))
for num in range(1, yrs):
    print("\t" + str(num) + "\t" + str(base))
    base = round(base + (increase * base), 2)

print("\n")

print("Exercise 3.8")
small = int(input("Enter the smaller number: "))
large = int(input("Enter the larger number: "))
while small != 0:
    temp = small + 0
    small = large % small
    large = temp + 0
print("The greatest common divisor is", large)

print("\n")
print("Exercise 3.9")
theSum = 0.0
numOfNums = 0
data = input("Enter a number: ")
while data != "":
    number = float(data)
    theSum += number
    numOfNums = numOfNums + 1
    data = input("Enter the next number: ")
print("The sum is", theSum)
avg = theSum /numOfNums
print("The average is", avg)

print("\n")
print("Exercise 3.10")
purchase = int(input("Enter the purchase price: "))
downPayment = .1 * purchase
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")
# for num in range(1,24):
