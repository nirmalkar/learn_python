totalBillAmount = input("Enter total bill amount ")
tipPercentage = input("what percent tip do you wanna give? ")
splitInPeople = input("How many people to split the bill ")
finalAmount = (totalBillAmount + (totalBillAmount * tipPercentage)/100)/splitInPeople
print("Each person will pay $",finalAmount)