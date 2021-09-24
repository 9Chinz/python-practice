#| Ex.2.1 1 จงเขียนโปรแกรมรับค่าของตัวเลข 1 ค่า (x) จากคีย์บอร์ด
#|          และทดสอบว่าเป็นเลขที่หารด้วย 5  ลงตัว หรือไม่ ตัวอย่าง
#|              Enter x: 10
#|              10 is divisible by 5.
#|              Enter x: 11
#|              11 is not divisible by 5.
x = int(input("enter x : "))
if x % 5 == 0:
    print(f"{x} is divisible by 5")
else:
    print(f"{x} not is divisible by 5")