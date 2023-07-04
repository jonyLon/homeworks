expression = input("Enter expression: ")

print(eval(expression))
if expression.find("+") != -1:
    list1 = expression.split("+")
    result = int(list1[0]) + int(list1[1])
elif expression.find("-") != -1:
    list1 = expression.split("-")
    result = int(list1[0]) - int(list1[1])
elif expression.find("/") != -1:
    list1 = expression.split("/")
    result = int(list1[0]) / int(list1[1])
elif expression.find("*") != -1:
    list1 = expression.split("*")
    result = int(list1[0]) * int(list1[1])

print(result)


import random

list1 = [random.randint(-100,100) for i in range(10)]
maxNum = max(list1)
minNum = min(list1)
countPositive = 0
countNegative = 0
countZero = 0
for i in list1:
    if i > 0:
        countPositive += 1
    elif i < 0: 
        countNegative += 1
    elif i == 0:
        countZero += 1
print("\tMax\tMin\tPositives\tNegatives\tZeros")
print("\t{}\t{}\t{}\t\t{}\t\t{}".format(maxNum,minNum,countPositive,countNegative,countZero))