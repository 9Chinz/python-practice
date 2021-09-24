#---------------------------------------------------
#* เราจะลองใช้ Dictionary กับ Function ในการทำโปรแกรมเครื่องคิดเลข
#---------------------------------------------------
#| Ex 6.1 ให้เขียนฟังก์ชันสำหรับ บวก ลบ คูณ และ หาร 

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def devide(n1, n2):
    return n1/n2

#| Ex 6.2 ให้สร้าง dictionary ชื่อ operations
#| ที่ใช้ key เป็นสัญญลักษณ์ + - * / และใช้ฟังก์ชันเป็น value

operations = {'+' : add, '-' : subtract, '*' : multiply, '/' : devide}


num1 = float(input("What's the first number? : "))

for symbol in operations:
    print(symbol)
choose_symbol = input("Choose symbol: ")

num2 = float(input("What's the second number? : "))

#---------------------------------------------------
#* จาก dictionary ที่สร้าง เราสามารถเรียกใช้ function ในรูปแบบนี้ได้
#* function = operations('+')
#* print(function(num1+num2))
#---------------------------------------------------

#| Ex 6.3 ให้เขียนโปรแกรม แสดงสัญญลักษณ์ + - * / ให้เลือก
#| และให้ผู้ใช้เลือก จากนั้นให้เรียก function ตามตัวอย่างข้างบนแล้วแสดงผล 

if choose_symbol not in operations:
    print("not in")
else:
    call_fucntion_symbol = operations[choose_symbol]
    print(call_fucntion_symbol(num1, num2))