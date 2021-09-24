'''
2.	ให้รับเวลาเข้าและออกของรถคันหนึ่ง (เปิดบริการตั้งแต่ 7:00 - 23:00) จากนั้นคำนวณค่าที่จอดรถที่ต้องจ่าย  โดยหลักเกณฑ์การคำนวณมีดังนี้ (สมมติว่าไม่มีการจอดข้ามวัน)
-	จอดรถไม่เกิน 15 นาที ไม่คิดค่าบริการ
-	จอดรถเกิน 15 นาที แต่ไม่เกิน 3 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
-	จอดรถตั้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
-	จอดรถเกิน 6 ชั่วโมงขึ้นไป เหมาจ่ายวันละ 200 บาท
ข้อมูลนำเข้า
        	มี 4 บรรทัด แต่ละบรรทัดมีจำนวนเต็มหนึ่งจำนวน
        	โดยบรรทัดที่ 1-2 เป็นชั่วโมงและนาทีของเวลาเข้า และบรรทัดที่ 3-4 เป็นชั่วโมงและนาทีของเวลา
ออก
ข้อมูลส่งออก
        	มีบรรทัดเดียว เป็นค่าที่จอดรถที่ต้องจ่าย ให้แสดงผลลัพธ์เป็นจำนวนเต็ม
7			7				7				7
0			0				30				30
7			7				10				13
15			16				31				31
=> 0		10				50				200
'''

hour_enter = int(input(""))
minute_enter = int(input(""))
hour_exit = int(input(""))
minute_exit = int(input(""))

if (hour_enter < 7 or hour_exit >= 23) or (minute_enter < 0 or minute_exit > 59):
	print("invalid hour please park between (7:00 - 23:00):")
else:
	if minute_exit == minute_enter:
		total_hours = hour_exit - hour_enter
		total_minutes = 0
	elif minute_exit > minute_enter:
		total_hours = hour_exit - hour_enter
		total_minutes = minute_exit - minute_enter
	else:
		total_hours = (hour_exit - hour_enter) - 1
		total_minutes = 60 - (minute_enter - minute_exit)

	parking_cost = 0

	if total_minutes <= 15 and total_hours <= 0:
		parking_cost = 0
	elif total_hours >= 6 and total_minutes > 0:
		parking_cost = 200
	elif total_hours <= 3:
		if total_minutes > 0 and total_hours == 3:
			total_hours += 2
		elif total_minutes > 0:
			total_hours += 1
		parking_cost = total_hours * 10
	elif 4 <= total_hours <= 6:
		if total_minutes > 0:
			total_hours += 1
		parking_cost = total_hours * 20

	print(f"=> {parking_cost}")