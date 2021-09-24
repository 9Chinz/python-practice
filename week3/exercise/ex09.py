'''
9.	ตัวเลข palindrome คือตัวเลขที่อ่านได้ทั้ง 2 ทาง แล้วมีค่าเท่ากัน เช่น 9009 โดย 9009 คือ palindrome ที่เกิดจากการคูณของตัวเลข 2 หลักที่มากที่สุด คือ 91x99 จงหา palindrome ที่มากที่สุดของตัวเลข 3 หลัก

100 * 100
100 * 101
...
100 * 999
101 * 100

'''
palindrome = 0
max_palindrome = 0
main = 0
times = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        number = str(i*j)
        number_reverse = number[::-1]
        if number_reverse == number:
            palindrome = int(number)
            if palindrome > max_palindrome:
                main = i
                times = j
                max_palindrome = palindrome
print(f"{main} x {times} = {max_palindrome}")