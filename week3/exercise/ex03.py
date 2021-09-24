'''
3.	2520 คือ ตัวเลขที่น้อยที่สุด ที่สามารถหารด้วยตัวเลขทุกตัวตั้งแต่ 1-10 จงหาจำนวนเต็มบวกที่น้อยที่สุดที่หารด้วยตัวเลขทุกตัวตั้งแต่ 1-20 
27720

232792560

--- 135.1695065498352 seconds ---
'''

number = 1
is_twenty = False
while not is_twenty:
    number += 1
    for divisor in range(1, 21):
        if number % divisor == 0:
            is_twenty = True
        else:
            is_twenty = False
            break
print(number)