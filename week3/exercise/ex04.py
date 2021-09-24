'''
4.	prime factors คือ ตัวเลขจำนวนเฉพาะที่คูณกันแล้วได้เท่ากับจำนวนที่กำหนด เช่น prime factors ของ 13195 คือ 5, 7, 13 และ 29 ให้เขียนโปรแกรมหา prime factor ที่มากที่สุดของ 600851475143
'''

number = 600851475143
prime_factors = []
sum_of_prime = 1
for divisor in range(2, number+1):
    if number % divisor == 0:
        prime_factors.append(divisor)
        sum_of_prime *= divisor
    
    if sum_of_prime == number:
        break

print(prime_factors[-1])