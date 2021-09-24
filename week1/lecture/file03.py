#| Ex.2.2 จงเขียนโปรแกรมรับข้อมูลจำนวน 2 ค่า คือ
#| คะแนน midterm และ final
#| ถ้าคะแนนรวมกัน > 50 แสดง pass ถ้าต่ำกว่าแสดง fail

m_score = int(input("Enter midterm score:"))
f_score = int(input("Enter final score:"))

total_score = m_score + f_score

if(total_score > 50):
    print("pass")
else:
    print("fail")