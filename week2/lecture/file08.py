#| Ex.3.1 จาก List ที่กำหนดให้ เป็นความสูงของนักเรียนในชั้น ให้หาค่าเฉลี่ยของความสูง
#| แสดงทศนิยม 2 ตำแหน่ง (ห้ามใช้ฟังก์ชัน)

height = [170, 165, 175, 172, 163, 169, 172, 155,162]

sum_of_height = 0
unit_of_height = len(height)
for h in height:
    sum_of_height += h

print(f"{sum_of_height/ unit_of_height:.2f}")