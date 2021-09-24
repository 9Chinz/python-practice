"""
9.	การหาคำตอบของสมการ ax^2 + bx +c = 0 สามารถหาได้โดยใช้สูตร 
จงเขียนโปรแกรม รับค่า a, b, c และคำนวณค่า x hint : การทำ square root ใช้ ยกกำลัง 0.5
"""

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
x = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
minus_x = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
print(f"x is {x} {minus_x}")