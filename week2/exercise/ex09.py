"""
!11.	อนุกรม Fibonacci คือ อนุกรมที่ตัวที่ 3 เป็นต้นไปเกิดจาก 2 ตัวหน้าบวกกัน จงเขียนโปรแกรมแสดงอนุกรม
เช่น ตั้งแต่ 0-1000 คือ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987
"""

end_num = int(input("Enter Fibonacci : "))
a = 0
b = 1

if end_num == 0:
    print(0)
elif end_num == 1:
    print(0, 1, 1, sep=", ")
elif end_num >= 2:
    print("0, 1", end="")
    for i in range(end_num):
        next = a + b
        a = b
        b = next
        if b >= end_num+1:
            break
        print(f", {next}", end="")
