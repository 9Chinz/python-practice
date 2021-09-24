"""
13.	จงเขียนโปรแกรมกำหนดราคา Pizza 
โดยถาดเล็ก 99 บาท ถาดกลาง 199 บาท ถาดใหญ่ 299 บาท 
และ หากต้องการเพิ่มขอบชีส ถาดเล็กจะบวกราคาอีก 20 บาท ถาดกลาง 30 บาท ถาดใหญ่ 40 บาท 
และ เพิ่มหน้าเป็นพิเศษอีก 20 บาท  ให้รับข้อมูลขนาด และ option เพิ่มชีส กับเพิ่มหน้า (Extra) และแสดงราคาสุดท้าย
small no cheese no extra = 99 + 0 + 0
small add cheese no extra = 99 + 20 + 0 = 119
small add cheese add extra = 99 + 20 + 20
Large add cheese add extra = 299 + 40 + 20 = 359
"""

size_of_pizza = input("Enter pizza size (S, M, L): ")
add_cheese = input("Do you want add cheese ? (Y/N): ")
add_extra = input("Do you want extra ? (Y/N): ")
total_price = 0

if(add_extra == "Y" or add_extra == "y"):
    total_price += 20

if size_of_pizza == "S" or size_of_pizza == "s":
    total_price += 99
    if(add_cheese == "Y" or add_cheese == "y"):
        total_price += 20
elif size_of_pizza == "M" or size_of_pizza == "m":
    total_price += 199
    if(add_cheese == "Y" or add_cheese == "y"):
        total_price += 30
elif size_of_pizza == "L" or size_of_pizza == "l":
    total_price += 299
    if(add_cheese == "Y" or add_cheese == "y"):
        total_price += 40
else:
    print("no size of pizza")
    total_price = 0

if(total_price > 0):
    print(f"Total price of pizza {total_price}")
