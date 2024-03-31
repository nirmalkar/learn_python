print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
def add_pep(pizza_size):
  if pizza_size == "S":
    return 2
  else:
    return 3
def add_cheese():
  return 1

def pizza_base_cost(size):
  if size == "S":
    return 15
  elif size == "M":
    return 20
  elif size == "L":
    return 25

def get_pizza_price(size, add_pepperoni, extra_cheese):
  if not size or not add_pepperoni or not extra_cheese:
    return "please put all the required stuffs!"
  
  if add_pepperoni == "N" and extra_cheese == "N":
    return pizza_base_cost(size)
  elif extra_cheese == "Y" and add_pepperoni == "N":
    return pizza_base_cost(size) + add_cheese()
  elif extra_cheese == "N" and add_pepperoni == "Y":
    return pizza_base_cost(size) + add_pep(size)
  elif extra_cheese == "Y" and add_pepperoni == "Y":
    return pizza_base_cost(size) + add_pep(size) + add_cheese()


price = get_pizza_price(size, add_pepperoni, extra_cheese)

print(f"Your final bill is: ${price}.")