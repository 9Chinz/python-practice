"""
4.	จงเขียนโปรแกรมรับค่าของตัวเลข 2 ค่า (x, y) จากคีย์บอร์ด และทดสอบเงื่อนไขว่า ค่าใดมากที่สุด โดยใช้ คําสัง if-else ตัวอย่างเช่น
Enter number 1: 10
Enter number 2: 35
Maximum is 35
"""
x = float(input("Enter number 1: "))
y = float(input("Enter number 2: "))

if(x == y):
    print(f"x, y is equal")
elif (x > y):
    print(f"Maximum is {x}")
else:
    print(f"Maximum is {y}")