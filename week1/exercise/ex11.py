"""
11.	รับจำนวนเต็ม 5 จำนวน คั่นด้วยช่องว่าง ตรวจว่าลำดับจากซ้ายไปขวาของจำนวนที่รับมา เรียงจากน้อยไปมากหรือไม่
ตอบ True, False
"""
number1, number2, number3, number4, number5 = [float(e) for e in input('Input: ').split()]

if number5 > number4 > number3 > number2 > number1:
    print(True)
else:
    print(False)