"""
5.	จงเขียนโปรแกรม เพื่อคํานวณค่าเฉลี่ย (Mean) ของข้อมูล (Input) 4 ค่าที่รับจากคีย์บอร์ด เพื่อเก็บในตัว แปร (x1, x2, x3, x4)  และแสดงผลลัพธ์ จากการคํานวณ เมื่อ Mean = (x1+x2+x3+x4) / 4
"""
x1 = int(input("x1: "))
x2 = int(input("x2: "))
x3 = int(input("x3: "))
x4 = int(input("x4: "))
mean = (x1+x2+x3+x4) / 4
print("mean = " + str(mean))