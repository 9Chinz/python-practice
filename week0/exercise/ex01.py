#1.	จงเขียนโปรแกรม เพื่อคํานวณหาพื้นที่ของสามเหลี่ยม Area = ½ x ฐาน x สูง  โดยมีข้อมูลเข้า  (Input) จากคีย์บอร์ด คือ ค่าของฐานของสามเหลี่ยม (b: Base) และค่าความสูงของสามเหลี่ยม (h: Height)  

base = int(input("Base: "))
height = int(input("Height: "))
area = 1/2 * base * height
print("Area = " + str(area))