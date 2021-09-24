
"""
1.	เขียนโปรแกรมเพื่อหาผลบวกของอนุกรม 5+10+15+20+… จนถึง n เมื่อ n เป็นตัวเลขที่รับเข้ามาทางคีย์บอร์ด

100
5+10+15+20+25+30+35+40+45+50 = 275
"""

end_number = int(input("Enter n number : "))

sum_of_number = 0

for number in range(0, end_number+1, 5):
    sum_of_number += number

print(f"sum of series = {sum_of_number}")