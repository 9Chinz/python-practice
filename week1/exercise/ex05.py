"""
5.	จงเขียนโปรแกรมรับค่าของตัวเลข 3 ค่า (a,b,c) จากคีย์บอร์ด และทดสอบเงื่อนไขว่า ค่าใดอยู่ตรงกลาง โดยใช้ คําสัง if-else 
*a
2 1 3 = 2
2 3 1 = 2
*b
1 2 3 = 2
3 2 1 = 2
*c
3 1 2 = 2
1 3 2 = 2

"""
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if b < a < c or c < a < b:
    print(f"a : {a}")
elif a < b < c or c < b < a:
    print(f"b : {b}")
else:
    print(f"c : {c}")