"""
4.	ให้ตรวจสอบว่า String ที่รับเข้ามาผ่านคีย์บอร์ด เป็นตัวอักษรพิมพ์เล็กทั้งหมด หรือตัวอักษรพิมพ์ใหญ่ทั้งหมด หรือมีทั้งตัวอักษรพิมพ์ใหญ่และพิมพ์เล็กผสมกันอยู่ อย่างละกี่ตัว 
Hello World

"""

lower_alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
count_lower_str = 0
count_upper_str = 0

text_input = input("Enter String : ")

for char in text_input:
    if char in lower_alphabet_list:
        count_lower_str += 1
    elif char in upper_alphabet_list:
        count_upper_str += 1

if count_lower_str == 0:
    print(f"Upper alphabets {count_upper_str}")
elif count_upper_str == 0:
    print(f"Lower alphabets {count_lower_str}")
else:
    print(f"Lower alphabets {count_lower_str} : Upper alphabets {count_upper_str}")



