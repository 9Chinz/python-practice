"""
8.	จงเขียนโปรแกรมรับตัวเลขของเดือน (1-12) จากคีย์บอร์ด และพิมพ์ผลลัพธ์ เป็นชื่อย่อของเดือน (1: Jan, 2:Feb, 3: Mar, 4:Apr, 5:May, 6:Jun, 7:Jul, 8:Aug, 9:Sep, 10:Oct, 11:Nov, 12:Dec) โดยใช list เช่น
Enter a number (1, 2, 3, …, or 12): 8 
Month : Aug
"""

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_number = int(input("Enter a number (1, 2, 3, ..., or 12): "))
if 1 <= month_number <= 12:
    print(f"Month : {month_list[month_number-1]}")
else:
    print("please enter month number between 1 and 12")
