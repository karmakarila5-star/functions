try:
    num1, num2 = eval(input("enter two numbers  separated by a coma : "))
    result = num1 / num2
    print("result is ", result)
except ZeroDivisionError:
    print("division by zero is error !!")
except SyntaxError:
    print("como is missing. enter numbers separated by comma like this 1, 2")
except:
    print("Wrong input")
else:
    print("no exception")
finally:
    print("this will execute no matter what")