y = input("Enter a number: ")
x = input("Enter a number: ")

# int is a function that converts a string to an integer
# so below we convert the input strings to integers to perform the operations

print(int(x) + int(y)) # addition
print(int(x) - int(y)) # subtraction | soustraction
print(int(x) * int(y)) # multiplication
print(int(x) / int(y)) # division
print(int(x) % int(y)) # modulo
print(int(x) ** int(y)) # exponentiation | exponentiation
print(int(x) // int(y)) # floor division | division entière

# we can also add the int from our input to perform the operations

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(a + b) # addition
print(a - b) # subtraction | soustraction
print(a * b) # multiplication
print(a / b) # division
print(a % b) # modulo
print(a ** b) # exponentiation | exponentiation
print(a // b) # floor division | division entière

# all of that is for int = full number, let's try with float = decimal number

c = float(input("Enter a number: "))
d = float(input("Enter a number: "))

print(c + d) # addition
print(c - d) # subtraction | soustraction
print(c * d) # multiplication
print(c / d) # division
print(c % d) # modulo
print(c ** d) # exponentiation | exponentiation
print(c // d) # floor division | division entière

# we can round the result of the division
print(round(c / d)) # division

# we can also format the result of the division to a specific number of decimal places
print("{g:.2f}".format(g = c / d)) # division

