"""
7.	ในคณิตศาสตร์ ตัวหารร่วมมาก หรือ ห.ร.ม. (greatest common divisor: gcd) ของจำนวนเต็มสองจำนวนซึ่งไม่เป็นศูนย์พร้อมกัน คือจำนวนเต็มที่มากที่สุดที่หารทั้งสองจำนวนลงตัว
จงหา ห.ร.ม. ของจำนวนเต็ม 2 จำนวนที่กำหนดให้
?ข้อมูลนำเข้า
!บรรทัดแรกเพียงบรรทัดเดียว ประกอบไปด้วยจำนวนเต็มบวกสองจำนวน a และ b มีค่าไม่เกิน 9999
*ข้อมูลส่งออก
!ในบรรทัดแรกของข้อมูลส่งออก ให้แสดงค่า ห.ร.ม. ของ a และ b
เช่น 	Input : 12 14		Output : 2
14 % 12 = 2 => 12 % 2 = 0 == 2
	Input : 7 3		Output : 1
	
"""

number1, number2 = [int(e) for e in input('Input : ').split()]

is_valid_number = True

if number1 > 9999 or number2 > 9999 or number1 <= 0 or number2 <= 0 :
	is_valid_number = False
	print("Please enter between 1-9999")

if is_valid_number:
	if number1 > number2:
		max_value = number1
	else:
		max_value = number2

	for i in range(1, max_value+1):
		if number1 % i == 0 and number2 % i == 0:
			gcd = i
	print(f"gcd of input is {gcd}")