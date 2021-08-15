name = input("Enter your fullname ")
lowerCasedName = name.lower()
s = lowerCasedName.count("s") 
m = lowerCasedName.count("m") 
a = lowerCasedName.count("a") 
r = lowerCasedName.count("r") 
t = lowerCasedName.count("t") 

total = s + m + a + r + t 
smartnessPercentage = (total / 5) * 100
print(type(smartnessPercentage))
if(smartnessPercentage >= 90):
    print("You are an Einstein! Go on celebrate!!")
elif(smartnessPercentage >= 60) and (smartnessPercentage <= 90):
    print(f"You are very smart. Your smartness percentage is {smartnessPercentage}")
elif(smartnessPercentage >= 30) and (smartnessPercentage <= 60):
    print(f"Your smartness percentage is {smartnessPercentage}")
else:
    print(f"Go eat almonds!")