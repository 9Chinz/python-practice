"""
8.	ให้เขียนโปรแกรมรับข้อมูลจาก Keyboard 2 ค่า คือ รหัสนักศึกษา และ ชื่อ จากนั้นแสดงผลในรูปแบบ  
"Student ID : [xx] Name : [nn] " ขึ้นบรรทัดใหม่ 
Year Entry : [แสดงปีที่รับเข้า] Last 4 Didit : [ ] Department : Computer Engineering 
6401 5030
"""
student_id = input("Student ID : ")
name = input("name : ")
year_entry = "25" + student_id[0:2]
print(f"Student ID : [{student_id}] Name : [{name}]")
print(f"Year Entry : [{year_entry}]] Last 4 Didit : [{student_id[4:]}] Department : Computer Engineering ")