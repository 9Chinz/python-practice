"""
7.	จงเขียนโปรแกรมรับค่าของตัวเลือก  1  ค่า  (x)  จากคีย์บอร์ด  และทดสอบว่า  จะหาพื้นที่สี่เหลี่ยม (Rectangle Area) หรือสามเหลี่ยม (Triangle Area) 
*ex1
Select 1. (Rectangle) or 2. (Triangle): 1
Enter width, length = _ , _ 
Rectangle Area = ???
*ex2
Select 1. (Rectangle) or 2. (Triangle): 2
Enter base, height = _ , _ 
Triangle Area = ???

"""
choice = int(input("Select 1. (Rectangle) or 2. (Triangle): "))

if choice == 1:
    #? Rectangle
    width, length = [float(e) for e in input("Enter width, length = ").split(',')]

    rectangle_area = width * length
    print(f"Rectangle Area = {rectangle_area}")
elif choice == 2:
    #? Triangle
    base, height = [float(e) for e in input("Enter base, height = ").split(',')]

    triangle_area = 1/2 * base * height
    print(f"Triangle Area = {triangle_area}")
else:
    print("Unknown choice")