#| Ex.2.3 จงเขียนโปรแกรมรับข้อมูลความเร็ว
#| ถ้าน้อยกว่า 45 แสดงผล slow speed
#| ถ้าระหว่าง  45 -> 90 แสดงผล moderate speed
#| ถ้ามากกว่า 90 ให้แสดงผล fast speed

speed = int(input("Enter speed : "))

if(speed < 45):
    print("slow speed")
elif(45 <= speed <= 90):
    print("moderate speed")
else:
    print("fast speed")