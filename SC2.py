#Name:Kayleigh Kennard
#Class: 6th Hour
#Assignment: SC2

import random
#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

weight=int(input("give me your weight in pounds"))
height=int(input("give me your height in inches"))
b=(weight/height**2)*703
print(b)
#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification
if b==18.5:
    print("you are underweight")
elif b<18.5 and b>=24.9:
    print("you are normal weight")
elif b>=25 and b<29.9:
    print("you are overweight")
elif b>=30:
    print("you are obese")


