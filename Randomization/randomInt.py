import random 

# random int between 0 and 10 (including 0 and 10)
random_int = random.randint(0, 10)

# random float number between 0 and 1 (does not include 1)
random_float = random.random()

# random float number between 0 and 4 (does not include 1)
random_float_between_0_4 = random.random() * 4

print(random_int)
print(random_float)
print(random_float_between_0_4)