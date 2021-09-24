#-----------------------------------------
#* Game of Rock Paper Scissors
#-----------------------------------------

#TODO-1: ให้ import random

import random

#TODO-2: รับ Input ว่าเป็น rock, paper, scissors

user_choice = input("Choose r : rock, p : paper, s : scissors | ")

#TODO-3: สร้าง List ของ rock, paper, scissors และให้คอมพิวเตอร์สุ่มเลือก

choice = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choice)

#TODO-4: แสดงผลว่าผู้เล่นเลือกอะไร และ คอมพิวเตอร์เลือกอะไร 

print(f"you {user_choice} : com {computer_choice}")

#TODO-1: เขียนโปรแกรม เพื่อตัดสินผู้ชนะ โดยมีหลักการดังนี้
#|       ถ้าเลือกเหมือนกันให้แสดง Both players selected [ตัวเลือก]. It's a tie!
#|       ถ้าผู้ใช้เลือก rock และ คอมพิวเตอร์เลือก scissors ให้แสดง Rock smashes scissors! You win!
#|       ถ้าผู้ใช้เลือก rock และ คอมพิวเตอร์ไม่เลือก scissors ให้แสดง Paper covers rock! You lose.
#|       ให้เขียนโปรแกรมลักษณะนี้ กับ กรณีที่เหลือ 
#|

#TODO-2: เมื่อจบเกมให้ถามผู้ใช้ว่า "Play again? (y/n): ถ้าผู้ใช้ตอบ y ก็ให้กลับไปเล่นใหม่ 