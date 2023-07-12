def output():
    print("\033[38;5;102m\"Don't compare yourself with anyone in this world...")
    print("\033[38;5;161mif \033[38;5;15myou \033[38;5;161mdo so\033[38;5;15m, you are insulting yourself.\033[38;5;102m\"")
    print("\033[38;5;15mBill Gates")
output()

def findPrimeNumsInRange(number1,number2):
    while number1 <= number2:
        if number1 % 2 == 0:
            print(number1)
        number1 += 1
findPrimeNumsInRange(2,25)

def drawSquare(len=10,symbol="$",full=True):
    for i in range(len):
        for j in range(len):
            if full:
              print(symbol,end=" ")
            else:
              print(" ",end=" ")
        print("|")
drawSquare(10,"*",False)

def minNum(a, b, c, d, f):
    list = [a, b, c, d, f]
    print(min(list))
minNum(10,15,6,25,60)


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


def countDigitsInNumber(n):
  print(len(str(n)))
countDigitsInNumber(1000)

def isPalindrome(n):
  string = str(n)
  length = int(len(string))
  half = int(length / 2)
  isPalindrome = False
  if string[0:half] == string[half:length][::-1]:
    isPalindrome = True
  return isPalindrome
    
print(isPalindrome(567765))
