#| Ex. 2.5 ปีอธิกสุรทิน หมายถึง ปีที่หารด้วย 4 แต่ปีที่หารด้วย 100 ลงตัวมิใช่ปีอธิกสุรทิน แต่ยกเว้นปีที่หารด้วย 400 ลงตัว
#| ค.ศ. 1600 และ 2000 เป็นปีอธิกสุรทิน แต่ ค.ศ. 1700, 1800 และ 1900 ไม่ใช่ 
#| ให้เขียนโปรแกรมรับปี แล้วบอกว่าเป็น ปีอธิกสุรทิน (Leap year) หรือไม่

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 400 == 0:
        print("Leap year")
    else:
        print("not leap year")
else:
    print("not leap year")

#| Ex. 2.7 จาก Ex. 2.5 ให้เขียนใหม่ให้มีจำนวนบรรทัดน้อยลง โดยใช้ AND OR NOT 