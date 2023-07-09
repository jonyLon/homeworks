import random
# 1
list = [random.randint(0, 100) for i in range(10)]
print(list)
indexOfMax = list.index(max(list))
indexOfMin = list.index(min(list))
if indexOfMax > indexOfMin:
  for i in range(indexOfMin+1,indexOfMax):
    list[i] *= 2
else:
  for i in range(indexOfMax+1,indexOfMin):
    list[i] *= 2
print(list)

# 2
list = [random.randint(0, 100) for i in range(10)]
print(list)
list1 = []
for i in range(0,9,2):
    print(i)
    list1.append(list[i+1])
    list1.append(list[i])

print(list1)
# 3
list = [65, 35, 17, 65, 27, 24, 65, 17, 78, 58]
repeatedNumbers = []
for i in list:
    count = 0
    for elem in list:
        if i == elem:
            count += 1           
    if(count > 1):
      if i not in repeatedNumbers:
        repeatedNumbers.append(i)
for i in repeatedNumbers:      
  print("Number:",i,"is repeated")

# 4
list = [[random.randint(0, 100) for i in range(4)] for i in range(3)]
print(list)
allSum = 0
for item in list:
    for i in item:
        print(i, end="  ")
    print(" | ", end="  ")
    print(sum(item), end=" ")
    print()
print("-"*25)
for i in range(4):
    verticalSum = 0
    for item in list:
      verticalSum += item[i]
    allSum += verticalSum
    print(verticalSum, end=" ")
print(" | ", end=" ")
print(allSum)
print()
# 5
letters = "abcdefgh"
numbers = range(1,9)

for el in letters:
    print(" ",el, end=" ",sep="")
print()
for i in numbers:
    for el in letters:
        if i == 3 and el == "d":
            print(" T ", end="")
        elif i == 3:
            print(" * ", end="")
        elif el == "d":
            print(" * ", end="")
        else:
          print("   ", end="")
    print(i)

# 6
for el in letters:
    print(" ",el, end=" ",sep="")
print()
for i in numbers:
    for el in letters:
        if i == 3 and el == "d":
            print(" O ", end="")
        elif i == 1 and el == "b" or i == 1 and el == "f" or i == 2 and el == "c" or i == 2 and el == "e" or i == 4 and el == "c" or i == 4 and el == "e" or i == 5 and el == "b" or i == 5 and el == "f" or i == 6 and el == "a" or i == 6 and el == "g" or i == 7 and el == "h":
            print(" * ", end="")
        else:
          print("   ", end="")
    print(i)

# 7
for el in letters:
    print(" ",el, end=" ",sep="")
print()
for i in numbers:
    for el in letters:
        if i == 3 and el == "d":
            print(" H ", end="")
        elif i == 1 and el == "c" or i == 1 and el == "e" or i == 2 and el == "b" or i == 2 and el == "f" or i == 4 and el == "b" or i == 4 and el == "f" or i == 5 and el == "c" or i == 5 and el == "e":
            print(" * ", end="")
        else:
          print("   ", end="")
    print(i)