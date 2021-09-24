"""
12.	รับจำนวนเต็ม 4 จำนวน คั่นด้วยช่องว่าง หาผลรวมของจำนวนที่รับมา โดยไม่รวมจำนวนที่ มากที่สุด และ น้อยที่สุด
10 20 30 40 = 20 + 30 = 50
10 20 40 30 = 20 + 30 = 50
10 40 20 30 = 20 + 30
20 30 10 40 = 20 + 30
40 10 20 30 = 20 + 30
"""
number1, number2, number3, number4 = [float(e) for e in input('Input: ').split()]

sum_of_all_number = 0

#* if all number are equal
if(number1 == number2 == number3 == number4):
    print("all number are equal")
    max_variable = ''
    min_variable = ''

#* find what variable is max
if number1 > number2 and number1 > number3 and number1 > number4:
    max_variable = 'number1'
elif number2 > number1 and number2 > number3 and number2 > number4:
    max_variable = 'number2'
elif number3 > number1 and number3 > number2 and number3 > number4:
    max_variable = 'number3'
elif number4 > number1 and number4 > number2 and number4 > number3:
    max_variable = 'number4'
else:
    pass

#* find what variable is min
if number1 < number2 and number1 < number3 and number1 < number4:
    min_variable = 'number1'
elif number2 < number1 and number2 < number3 and number2 < number4:
    min_variable = 'number2'
elif number3 < number1 and number3 < number2 and number3 < number4:
    min_variable = 'number3'
elif number4 < number1 and number4 < number2 and number4 < number3:
    min_variable = 'number4'
else:
    pass

#* check what variable is max, min and plus only number that not max and min
if max_variable == 'number1' and min_variable == 'number2' or max_variable == 'number2' and min_variable == 'number1':
    sum_of_all_number = number3 + number4
elif max_variable == 'number1' and min_variable == 'number3' or max_variable == 'number3' and min_variable == 'number1':
    sum_of_all_number = number2 + number4
elif max_variable == 'number1' and min_variable == 'number4' or max_variable == 'number4' and min_variable == 'number1':
    sum_of_all_number = number2 + number3
elif max_variable == 'number2' and min_variable == 'number3' or max_variable == 'number3' and min_variable == 'number2':
    sum_of_all_number = number1 + number4
elif max_variable == 'number2' and min_variable == 'number4' or max_variable == 'number4' and min_variable == 'number2':
    sum_of_all_number = number1 + number3
elif max_variable == 'number3' and min_variable == 'number4' or max_variable == 'number4' and min_variable == 'number3':
    sum_of_all_number = number1 + number2
else:
    pass

if(sum_of_all_number > 0):
    print(sum_of_all_number)
