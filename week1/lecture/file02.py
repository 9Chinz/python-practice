### ตัวอย่าง : ในสวนสนุกแห่งหนึ่งมีอัตราการเข้าชมต่างกันตามอายุ
### ถ้าต่ำกว่า 4 ขวบ ฟรี
### อายุ 4-18 = 25 บาท
### อายุ 18-65 = 40 บาท
### อายุ > 65 = 20 บาท
### จงเขียนโปรแกรมรับอายุแล้วคำนวณจำนวนเงิน
age = int(input("Enter your age : "))

if age <= 4:
    price = 0
elif age <= 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is {price}.")