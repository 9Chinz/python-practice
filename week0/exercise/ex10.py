"""
10.	เขียนโปรแกรมคำนวณหลักสุดท้ายของบัตรประชาชน
"""

idcard = input("Enter ID Card (12 digit) : ")
sum_digit =  ((int(idcard[0])*13) + (int(idcard[1])*12) + (int(idcard[2])*11) + (int(idcard[3])*10) + (int(idcard[4])*9) + (int(idcard[5])*8) + (int(idcard[6])*7) + (int(idcard[7])*6) + (int(idcard[8])*5) + (int(idcard[9])*4) + (int(idcard[10])*3) + (int(idcard[11])*2))
check_digit = str(11 - (sum_digit % 11))
print(f"last digit is {check_digit}")