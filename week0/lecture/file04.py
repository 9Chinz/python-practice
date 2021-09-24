#| Ex1.8 จากคำสั่งข้างต้นให้ใส่วงเล็ก เพื่อให้ผลลัพธ์เป็น 3.0 


#| Ex1.9 จงเขียนโปรแกรมหาBody Mass Index (BMI) 
#|       = weight(kg) / height(m)^2 
#| Input:
#|      Enter weight : 80
#|      Enter height : 1.75
#|Output:
#|      80 ÷ (1.75 x 1.75) = 26.122448979591837
#|      BMI = 26

weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = weight / height**2
print("BMI = ", int(bmi))