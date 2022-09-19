print(len("Hello world"))

# subscripting
print("Hello world"[0])

print(1)

print("integer hai ki nahi", type(1) == "int")

# type conversion
name = input("Please enter you name")
intro = f"{name} is"
age = 28
checkIndian = input("are you Indian y/n ")
if checkIndian == "y":
    isIndian = True
else:
    isIndian = False
ageInStr = str(age)
print(intro + ageInStr)


# f-string
print(f"{intro} {age} years old, is Indian: {isIndian}.")
