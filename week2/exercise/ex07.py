"""
!9.	จงเขียนโปรแกรมที่คำนวณค่าของ a+aa+aaa+aaaa เมื่อรับข้อมูลเป็นตัวเลข 1 หลัก 
Input : 9
Output : 11106 (=9+99+999+9999)
Input : 1
Output : 1234 = 1+11+111+1111
"""
number = int(input("Enter number : "))

print(f"Output : {(number*1)+(number*11)+(number*111)+(number*1111)} = ({(number*1)}+{(number*11)}+{(number*111)}+{(number*1111)})")