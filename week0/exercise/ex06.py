#6.	จงเขียนโปรแกรม อ่านจำนวนจริง 5 จำนวน คั่นด้วยช่องว่าง คำนวณค่าเฉลี่ยของจำนวนทั้งห้า แล้วแสดงค่าเฉลี่ย
x1, x2, x3, x4, x5 = [float(e) for e in input("input: ").split()]
mean = (x1+x2+x3+x4+x5) / 5
print(f"mean = {mean:.3f}")