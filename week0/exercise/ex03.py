"""
3.	จงเขียนโปรแกรม เพื่อรับค่าของเวลาปัจจุบัน 3 ค่า คือ ชั่วโมง (Hour), นาที (Min), และวินาที (Sec) เป็น ข้อมูลเข้า (Input) จากคีย์บอร์ด และพิมพ ค่าของเวลานั้น ในรูปแบบ hh:mm:ss ตัวอย่างเช่น
ENTER current Hour = 10 
ENTER current Min = 45 
ENTER current Sec = 5 
Current time is 10:45:05
"""

hour = int(input("ENTER current Hour = "))
min = int(input("ENTER current Min = "))
sec = int(input("ENTER current Sec = "))

print(f"Current time is {hour:02d}:{min:02d}:{sec:02d}")