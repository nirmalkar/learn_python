age = input("What is your age? ")
maxLiveDurationInDays = 365 * 90
print(maxLiveDurationInDays)

daysLived = int(age) * 365
daysLeft = maxLiveDurationInDays - daysLived
statement = f"If you are lucky then you have {daysLeft} days left to live!!"
print(statement)