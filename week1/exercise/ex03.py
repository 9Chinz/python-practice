"""
3.	จงเขียนโปรแกรม เพื่อคํานวณคะแนนรวมของผลสอบวิชา Programming จากคะแนน Mid-term (100 คะแนน), คะแนน Final (100 คะแนน), และคะแนน Homework (10 คะแนน) เป็นข้อมูลเข้า (Input) จากคีย์บอร์ด และแสดงผลลัพธ์ จากการคํานวณ เมื่อ
คะแนนรวม (x) = Mid-term (40%) + Final (50%) + HW (10%) และตัดเกรดตามเงื่อนไขต่อไปนี้
คะแนน	90 <= x <= 100	ได้เกรด ‘A’                  100 => A
คะแนน	85 <= x < 90		ได้เกรด ‘B+’             90 => A
คะแนน	80 <= x < 85		ได้เกรด ‘B’              85 => B+
คะแนน	70 <= x < 80		ได้เกรด ‘C+’ 
คะแนน	60 <= x < 70		ได้เกรด ‘C’ 
คะแนน	55 <= x < 60		ได้เกรด ‘D+’ 
คะแนน	50 <= x < 55		ได้เกรด ‘D’ 
คะแนน	x < 50			ได้เกรด ‘F’
"""

mid_term = float(input("Enter Mid-term score: "))*40 / 100
final = float(input("Enter Final score: "))*50 / 100
homework = float(input("Enter Homework score: "))

total_score = mid_term + final + homework

if( 0 <= mid_term <= 40 or 0 <= final <= 50 or 0 <= homework <= 10):
    if total_score < 50:
        print(f"คะแนน {total_score} ได้เกรด ‘F’")
    elif total_score < 55:
        print(f"คะแนน {total_score} ได้เกรด ‘D’")
    elif total_score < 60:
        print(f"คะแนน {total_score} ได้เกรด ‘D+’")
    elif total_score < 70:
        print(f"คะแนน {total_score} ได้เกรด ‘C’")
    elif total_score < 80:
        print(f"คะแนน {total_score} ได้เกรด ‘C+’")
    elif total_score < 85:
        print(f"คะแนน {total_score} ได้เกรด ‘B’")
    elif total_score < 90:
        print(f"คะแนน {total_score} ได้เกรด ‘B+’")
    elif total_score <= 100:
        print(f"คะแนน {total_score} ได้เกรด ‘A’")
    else:
        print("please enter score between (0, 100)")
else:
    print("please enter correct score Mid-term (100 คะแนน), คะแนน Final (100 คะแนน), และคะแนน Homework (10 คะแนน)")