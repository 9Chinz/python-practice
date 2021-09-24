"""
### ตัวอย่าง 
* ให้รับเวลาเข้าและออกของรถคันหนึ่ง (เปิดบริการตั้งแต่ 7:00 - 23:00) จากนั้นคำนวณค่าที่จอดรถที่ต้องจ่าย
* โดยหลักเกณฑ์การคำนวณมีดังนี้
        1. จอดรถไม่เกิน 15 นาที ไม่คิดค่าบริการ
        2. จอดรถเกิน 15 นาที แต่ไม่เกิน 3 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
        3. จอดรถตั้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
        4. จอดรถเกิน 6 ชั่วโมงขึ้นไป เหมาจ่ายวันละ 200 บาท
## ข้อมูลนำเข้า
        มี 4 บรรทัด แต่ละบรรทัดมีจำนวนเต็มหนึ่งจำนวน
        โดยบรรทัดที่ 1-2 เป็นชั่วโมงและนาทีของเวลาเข้า และบรรทัดที่ 3-4 เป็นชั่วโมงและนาทีของเวลาออก
## ข้อมูลส่งออก
        มีบรรทัดเดียว เป็นค่าที่จอดรถที่ต้องจ่าย ให้แสดงผลลัพธ์เป็นจำนวนเต็ม
|ตัวอย่าง
        7
        0
        7
        15
*       => 0
        7
        0
        7
        16
*       => 10
        7
        30
        10
        31
*       => 50
        7
        30
        13
        31
*       => 200
"""
start_parking_hour = int(input(""))
start_parking_minute = int(input(""))
stop_parking_hour = int(input(""))
stop_parking_minute = int(input(""))

total_parking_hour = stop_parking_hour - start_parking_hour
total_parking_minute = stop_parking_minute - start_parking_minute
parking_price = 0

if start_parking_hour not in range (7, 23) or stop_parking_hour not in range (7, 23):
        print('you can park between(7:00 - 23:00) ')

if total_parking_hour == 0 and total_parking_minute <= 15:
        print("0")
elif total_parking_hour <= 3:
        print(f"hour {total_parking_hour} minute {total_parking_minute}")
        total_parking_hour += 1
        if total_parking_hour > 1 and total_parking_minute > 0:
                total_parking_hour += 1
        parking_price = total_parking_hour * 10
        print(parking_price)
elif total_parking_hour < 6:
        print(f"hour {total_parking_hour} minute {total_parking_minute}")
elif total_parking_hour >= 6:
        if total_parking_minute > 0:
                
        print(f"hour {total_parking_hour} minute {total_parking_minute}")
        print(200)