"""
9.	จงเขียนโปรแกรมรับค่าของเลขจำนวนเต็ม (N) จากคีย์บอร์ด และพิมพ์ตัวเลขตัวสุดท้ายของ N เป็น
ข้อความ (เช่น 0:Zero, 1:One, 2:Two, 3:Three, 4:Four, 5:Five, 6:Six, 7:Seven, 8:Eight, 9:Nine) โดยใช้ List  
แนะนํา : การหาตัวเลขตัวสุดท้ายของเลขจำนวนเต็มใดๆ (N) สามารถทำได้ ด้วยการ หาเศษที่ได้จากการ
หารด้วย 10 ของ N (คือ N%10) ตัวอย่างเช่น
Enter an integer N = 512 
2: Two
"""

number_in_string_list = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

number = int(input("Enter an integer N = "))
if(number < 0):
    digit_one = (-number) % 10
else:
    digit_one = number % 10
    
print(f"{digit_one}: {number_in_string_list[digit_one]}")