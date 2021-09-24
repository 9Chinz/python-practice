#| Ex 1.13 สมมติว่าเราจะอยู่จนถึงอายุ 90 ปี 
#| คำนวณหา ว่าเราจะมีเวลาเหลืออีกเท่าไร ให้ใช้ f-string
#| Input:
#|      Enter age : 56
#|Output:
#|      You have 12410 days, 1768 weeks, and 408 months left.

age = int(input("Enter age : "))
left_age = 90 - age
print(f"{'':>4}You have {left_age*365} days, {left_age*52} weeks, and {left_age*12} months left.")