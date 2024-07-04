def calculator():

  try:
    a = float(input("Enter first num:"))
    b = float(input('enter second num:'))
    c = input("enter the operation: +,-,*,/ :")

    if c == '+':
        ans = (a+b)
    elif c == '-':
        ans = (a-b)
    elif c == '*':
        ans = (a*b)
    elif c == '/':
        ans = (a/b)
    else:
        print("Its an invalid operation!")
    print("result:", ans)
  except ZeroDivisionError:
    print("cannot divide by zero")
  except ValueError:
    print("please enter only numbers")


calculator()
