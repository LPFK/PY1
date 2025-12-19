interpreter = input("Enter a arithmetic expression : ")
interpreter = interpreter.strip()
interpreter = interpreter.split(" ")
if interpreter[1] == "+":
    print(int(interpreter[0]) + int(interpreter[2]))
elif interpreter[1] == "-":
    print(int(interpreter[0]) - int(interpreter[2]))
elif interpreter[1] == "*":
    print(int(interpreter[0]) * int(interpreter[2]))
elif interpreter[1] == "/":
    print(int(interpreter[0]) / int(interpreter[2]))    