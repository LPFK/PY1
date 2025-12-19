text = input("Input: ")
vowels = "aeiouAEIOU"
result = ""
for char in text:
    if char not in vowels:
        result += char
print(f"Output: {result}")
