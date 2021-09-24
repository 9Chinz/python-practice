
#! a เรี่ม 65 => 128
""" 
#08b b เป็น base 2 , 8 หลัก
o เลข base 8 
4 ตัว , x เลข base 16 
X เลข base 16 ไม่มี 0x นำหน้า 
c เอา ascii ของเลขตัวนั้นมาแสดง 
"""
for i in range(65, 128):
        print(f"{i:3} {i:#08b} {i:04o} {i:#x} {i:X} {i:c}")