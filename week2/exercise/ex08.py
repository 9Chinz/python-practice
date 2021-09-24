"""
!10.	แปลงเลขโรมัน เป็นเลขอารบิก เช่น MMMDCCXXIV = 3724 (ค้นหาวิธีทางทางอินเตอร์เน็ต)
1000 + 1000 + 1000 + 500 + 100 + 100 + 10 + 10 + 1 - 5
XCVIII

! IIIV
D C - 100
I D += 500
V I += -1
"""

roman_number = input("Enter Roman number : ")

roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
arabic_value = 0

for i in range(len(roman_number)):
    if i+1 != len(roman_number) and roman_value[roman_number[i+1]] > roman_value[roman_number[i]] :
        arabic_value -= roman_value[roman_number[i]]
    else:
        arabic_value += roman_value[roman_number[i]]
print(f"Roman number {arabic_value}")