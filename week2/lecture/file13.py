#| Ex 3.6 ให้เขียนโปรแกรมคำนวณ Factorial
#|        Factorial 5 = 5x4x3x2x1

start_number = int(input("enter fac : "))
sum_factorial = 1
for fac in range(start_number, 0, -1):
    sum_factorial *= fac
print(sum_factorial)