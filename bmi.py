# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(weight / height ** 2)
bmi = round((weight / height ** 2), 2)
if(bmi < 18.5):
  print(f'Your BMI is {bmi}, you are underweight.')
elif(bmi < 25):
  print(f'Your BMI is {bmi}, you are normal weight.')
elif(bmi < 30):
  print(f'Your BMI is {bmi}, you are slightly overweight.')
elif(bmi < 35):
  print(f'Your BMI is {bmi}, you are obese.')
elif(50 > bmi >= 35):
  print(f'Your BMI is {bmi}, you are clinically obese.')
else:
  print('Are you for real?')