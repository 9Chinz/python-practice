"""
6.	จงเขียนโปรแกรมจัดกลุ่มของคนตามอายุ (Age) ที่มีเงื่อนไขดังนี้ 
กลุ่มเด็ก (Children)		อายุ 0 – 10 ปี
กลุ่มวัยรุ่น (Teenage)		อายุ 11 – 20 ปี
กลุ่มวัยทำงาน (Adult)		อายุ 21 – 35 ปี 
กลุ่มวัยกลางคน (Middle age) 	อายุ 36 – 55 ปี 
กลุ่มสูงวัย (Old age)		อายุ 56 ปีขึ้นไป
"""
age = int(input("Enter age : "))

if 0 <= age <= 10:
    print("Children")
elif 10 < age <= 20:
    print("Teenage")
elif 20 < age <= 35:
    print("Adult")
elif 35 < age <= 55:
    print("Middle age")
elif age > 55:
    print("Old age")
else:
    print("please no minus age")