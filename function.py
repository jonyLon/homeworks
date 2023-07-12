# 1
def output():
    print("\033[38;5;102m\"Don't compare yourself with anyone in this world...")
    print("\033[38;5;161mif \033[38;5;15myou \033[38;5;161mdo so\033[38;5;15m, you are insulting yourself.\033[38;5;102m\"")
    print("\033[38;5;15mBill Gates")
output()
# 2
def findPrimeNumsInRange(number1,number2):
    while number1 <= number2:
        if number1 % 2 == 0:
            print(number1)
        number1 += 1
findPrimeNumsInRange(2,25)
# 3
def drawSquare(len=10,symbol="$",full=True):
    for i in range(len):
        for j in range(len):
            if full:
              print(symbol,end=" ")
            else:
              if i == 0 or i == len-1 or j == 0 or j == len-1: 
                print(symbol,end=" ")
              else:
                print(" ",end=" ")
        print()
drawSquare(10,"*",False)
# 4
def minNum(a, b, c, d, f):
    list = [a, b, c, d, f]
    print(min(list))
minNum(10,15,6,25,60)

# 5
def multiplyNumsInRange(number1,number2=1):
    mult = 1
    if number1 > number2:
      start = number2
      end = number1
      while start < end:
        mult *= start
        start += 1
      print(mult)
    else:
      while number1 < number2:
        mult *= number1
        number1 += 1
      print(mult)
multiplyNumsInRange(6)

# 6
def countDigitsInNumber(n):
  return len(str(n))
countDigitsInNumber(1000)
# 7
def isPalindrome(n):
  string = str(n)
  length = int(len(string))
  half = int(length // 2)
  isPalindrome = False
  for i in range(half):
    if string[i] == string[-i]:
      isPalindrome = True
  return isPalindrome
    
print(isPalindrome(5678765))


def isPalindrome(n):
  length = countDigitsInNumber(n)
  for i in range(length//2):
    size = countDigitsInNumber(n)
    first = n // (10**(size - 1))
    last = n % 10
    if first != last: 
      return False
    n = (n % (10**(size - 1)))//10
  return True
print(isPalindrome(56755765))