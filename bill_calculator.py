totalBillAmount = input("Enter total bill amount ")
tipPercentage = input("what percent tip do you wanna give? ")
splitInPeople = input("How many people to split the bill ")
print(type(totalBillAmount))
finalAmount = (
    int(totalBillAmount) + (int(totalBillAmount) * int(tipPercentage)) / 100
) / int(splitInPeople)
print("Each person will pay $", finalAmount)
