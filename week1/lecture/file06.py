#|Ex. 2.4 จากโปรแกรม BMI Calcularor 
#|       = weight(kg) / height(m)^2 
#| Input:
#|      Enter weight : 80
#|      Enter height : 1.75
#| Output:
#|      BMI = 26
#| นอกจากจะบอกค่า BMI แล้ว ยังให้คำแนะนำดังนี้

#|    Under 18.5 they are underweight
#|    Over 18.5 but below 25 they have a normal weight
#|    Over 25 but below 30 they are slightly overweight
#|    Over 30 but below 35 they are obese
#|    Above 35 they are clinically obese.

weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in m : "))

bmi = weight / height**2

print(f"your bmi {bmi}")
if bmi < 18.5:
    print("Under 18.5 they are underweight")
elif bmi < 25:
    print("Over 18.5 but below 25 they have a normal weight")
elif bmi < 30:
    print("Over 25 but below 30 they are slightly overweight")
elif bmi <= 35:
    print("Over 30 but below 35 they are obese.")
else:
    print("Above 35 they are clinically obese.")