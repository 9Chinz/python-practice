#| Ex. 2.6 มีตัวแปร 3 ตัว คือ a,b,c (เขียนได้ 2 แบบ)
#| ให้เขียนโปรแกรมหาตัวแปรใดที่เก็บค่ามากที่สุด โดยใช้ if

a=20
b=10
c=30

if a > b and a > c:
    print("a is max")
elif b > c and b > a:
    print("b is max")
else:
    print("c is max")