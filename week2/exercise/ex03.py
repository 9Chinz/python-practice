"""
3.	เขียนโปรแกรม n เป็นตัวเลขที่รับเข้ามาทางคีย์บอร์ด และหาผลรวมของตัวเลขที่หารด้วย 2 หรือ 3 ไม่ลงตัว ยกเว้นตัวเลขที่หารด้วย 2 และ 3 ลงตัว 

1 == 1
2
3 
4
5 == 1

6 == 1
7 == 1
8
9
10
"""

n = int(input("Enter n : "))

sum_of_num = 0

for number in range(1, n+1):
    if (number % 2 == 0 and number % 3 == 0) or (number % 2 != 0 and number % 3 != 0): 
        print(f"{number}", end=" ")
        sum_of_num += number

print(f"sum of num = {sum_of_num}")
