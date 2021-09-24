"""
2.	จงเขียนโปรแกรมรับค่าของคะแนนเป็นจำนวนเต็ม (x) จากคีย์บอร์ด และตัดเกรดตามเงื่อนไขต่อไปนี้ 
คะแนน      80 <= x <= 100	ได้เกรด	‘G’    หมายถึง   Good
คะแนน      50 <= x < 80     	ได้เกรด ‘P’     หมายถึง   Pass 
คะแนน      0 <= x < 50         	ได้เกรด ‘F’     หมายถึง   Fail
"""
score = float(input("Enter score : "))

if 0 <= score < 50:
    print("ได้เกรด ‘F’")
elif score < 80:
    print("ได้เกรด ‘P’")
elif score <= 100:
    print("ได้เกรด	‘G’")
else:
    print("Input score between (0 - 100)")