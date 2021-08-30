def print_Name(name):
    print(name)

print_Name("Hemant")

# print name it's num of letter times (while loop)
def print_name_letter_times_while(name):
    name_length = len(name)
    while name_length > 0:
        print(name)
        name_length -= 1

# print name it's num of letter times (for loop)
def print_name_letter_times_for(name):
    arr = [char for char in name] # or we can use predefined function list(name), this would also do the same work
    for char in arr:
        print(name)

print_name_letter_times_while("Monty")
print_name_letter_times_for("Davinci")