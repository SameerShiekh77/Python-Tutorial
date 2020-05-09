print("CALCULATOR DEVELOP BY IT EDUCATION\n\n\n\n")


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
op = input("Select your operator\n\t+\t-\t*\t/\t%\n")

if op == '+':
    {
        print("The sum of num1 and num2 is: ", num1  + num2)
    }
elif op == '-':
    {
        print("The subtraction of num1 and num2 is: ", num1  - num2)
    }
elif op == '*':
    {
        print("The multiplication of num1 and num2 is: ", num1  * num2)
    }
elif op == '/':
    {
        print("The division of num1 and num2 is: ", num1  / num2)
    }
elif op == '%':
    {
        print("The remainder of num1 and num2 is: ", num1  % num2)
    }

else:
    print("Invalid Operator")