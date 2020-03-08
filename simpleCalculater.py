print("----------Simple Cal---------")
inValid = True
operations = ("*", "/", "-", "+")
operation = ""
number1 = 0
number2 = 0
ans = 0

# First Number
while inValid:
    number1 = input("Please Enter the First Number : ")
    if number1.isnumeric():
        inValid = False
        number1 = int(number1)
    else:
        print("Please Enter Valid Number")
        inValid = True

# Operation
inValid = True
while inValid:
    operation = input("Please Enter the Operation : ")
    if operation in operations:
        inValid = False
    else:
        print("Please Enter Valid Operation")
        inValid = True

# Second Number
inValid = True
while inValid:
    number2 = input("Please Enter the Second Number : ")
    if number2.isnumeric():
        inValid = False
        number2 = int(number2)
        if operation == operations[1] and number2 == 0:
            print("Number can not equal to Zero")
            inValid = True
    else:
        print("Please Enter Valid Number")
        inValid = True

if operation == operations[0]:
    ans = number1 * number2
elif operation == operations[1]:
    ans = number1 / number2
elif operation == operations[2]:
    ans = number1 - number2
elif operation == operations[3]:
    ans = number1 + number2

print("Answer For " + str(number1) + operation + str(number2) + " : " + str(ans))
