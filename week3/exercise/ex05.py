'''
5.	จำนวนเฉพาะ (Prime Number) คือตัวเลขที่มีแต่ 1 กับตัวมันเองที่หารลงตัว โดยจำนวนเฉพาะ 6 ตัวแรกคือ 2, 3, 5, 7, 11, 13 โดยจำนวนเฉพาะตัวที่ 6 คือ 13 จงหาจำนวนเฉพาะตัวที่ 1001 
'''

prime_position = 1
prime_value = 0
number = 2

while True:
    divided_count = 0
    if prime_position == 1002:
        break
    for divisor in range(1, number+1):
        if number % divisor == 0:
            divided_count += 1
    if divided_count == 2:
        prime_value = number
        prime_position += 1
    number += 1

print(f"position  => {prime_position-1} : value => {prime_value}")