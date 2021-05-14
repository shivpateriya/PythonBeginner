#add
def add( n1,n2):
   return n1+n2

#subtract
def sub(n1,n2):
   return n1-n2

#multiply

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2


def calculator():
 
  operator={'+' :add,
  '-' :sub,
  '*':mul,
  '/': div
  }
  cal_Continue = True
  num1=float(input('Enter first number  : '))
  while cal_Continue:
    for i in operator:
      print(i)
    symbol=input('Enter symbol : ')  
    num2=float(input('Enter next number : '))  
  
    calculate =operator[symbol]
    answer =calculate(num1,num2)
    
    print(f"{num1} {symbol} {num2} = {answer}")
    if input('Enter y to continue and, N to exit : ')=='y':
      num1 = answer
    else:
      cal_Continue =False
      calculator()
calculator()         




