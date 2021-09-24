"""
4.	จงเขียนโปรแกรม เพื่อคํานวณคะแนนรวมของผลสอบวิชา Programming จากคะแนน Mid-term, คะแนน Final, และคะแนน Homework เป็นข้อมูลเข้า (Input) จากคีย์บอร์ด และแสดงผลลัพธ์จากการ คํานวณ เมื่อ
คะแนนรวม (Total) = Mid-term (40%) + Final (50%) + HW (10%)
mid-term 100 final 100 hw 100
40 ของ 100
50 ของ 100
10 ของ 100
มาเฉลี่ยเอา 
"""
mid_term = int(input("Mid-term: "))*40 / 100
final = int(input("Final: "))*50 / 100
homework = int(input("Homework: "))*10 / 100
total = mid_term + final + homework
print("Total = " + str(total))