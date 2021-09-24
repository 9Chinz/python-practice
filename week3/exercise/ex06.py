'''
6.	sum of the squares ของ 1-10 คือ 
1^2 + 2^2 + ... + 10^2 = 385
ส่วน square of the sum 1-10 คือ
(1+2+..+10)^2 = 55^2 = 3025
ผลต่างระหว่าง square of the sum กับ sum of the squares = 3025-385 = 2640 ให้หาผลต่างของ square of the sum กับ sum of the squares ของ 1-100 
25164150
'''
sum_of_squares = 0
square_of_sum = 0

for number in range(1, 101):
    sum_of_squares += (number**2)
    square_of_sum += number

result = ((square_of_sum)**2) - sum_of_squares
print(result)