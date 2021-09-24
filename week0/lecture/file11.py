#| Ex 1.14 ให้คำนวณว่าโปรโมชั่น มา 4 จ่าย 3 จะจ่ายเท่าไร
#| ให้รับ จำนวนเงินต่อหัว และ จำนวนคนที่ไป 

amount_of_person = int(input("Input amount of person : "))
price_per_person = float(input("Input price/person (baht) : "))
discount_per_person = price_per_person - (price_per_person * 0.25)
print(f"Should pay {amount_of_person * price_per_person} instead pay {amount_of_person * discount_per_person}")