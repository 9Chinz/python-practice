#---------------------------------------------------
#* https://poki.com/th/g/hangman
#* https://hangmanwordgame.com/?fca=1&success=0#/
#---------------------------------------------------
#* ในไฟล์นี้จะเป็นการเขียน hangman โดยให้เริ่มจากการเขียน flowchart 
#* เข้าไปที่เว็บ https://www.draw.io/ 

#| Ex 4.6 Hangman Step 1 ให้ทำงานใน TODO ให้ครบทั้ง 3 ข้อ

#TODO-1 - สุ่มเลือกคำจาก word_list และใส่ในตัวแปรชื่อ chosen_word.
#TODO-2 - ถามผู้ใช้ให้เดาตัวอักษร 1 ตัว แล้วเก็บในตัวแปรชื่อ guess. และแปลงเป็น lowercase.
#TODO-3 - ตรวจสอบว่าตัวอักษรที่ผู้ใช้เดา อยู่ในอักขระตัวตัวหนึ่งใน chosen_word หรือไม่
#TODO-4: - สร้าง List ว่าง และตั้งชื่อว่า display.
#* ให้เพิ่ม '_' ใน list display เท่ากับจำนวนตัวอักษรใน chosen_word
#* เช่น หาก chosen_word เป็น "apple", display จะเป็น ["_", "_", "_", "_", "_"]
#TODO-5: - วน Loop ไปแต่ละตำแหน่งใน chosen_word
#* ถ้าตัวอักษรในตำแหน่งนั้นตรงกับ 'guess' ให้เปลี่ยนตัวอักษรใน display เป็น guess ในตำแหน่งเดียวกัน
#* เช่น ถ้าผู้ใช้ป้อน "p" และ chosen word เป็น "apple" display ควรจะเป็น ["_", "p", "p", "_", "_"].
#TODO-6: - แสดง 'display' และดูว่าตัวที่เดาถูกตำแหน่ง และตัวอื่นยังคงเป็น "_".
#TODO-7: - ใช้ while loop เพื่อให้ผู้ใช้เดาตัวอักษรไปเรื่อยๆ โดย loop หยุดเมื่อเดาครบทุกตัวและไม่มี "_"
#TODO-8: - สร้างตัวแปร 'lives' เพื่อเก็บจำนวนชีวิต
#|Set 'lives' to equal 6.
#TODO-9: - ถ้าอักษรที่เดาไม่ใช่อักษรใน chosen_word
#|         ให้ลดค่า 'lives' ลง 1. 
#|         ถ้า lives เหลือ 0 จบเกมและแสดง "You lose."
#TODO-10: - พิมพ์ ASCII art จาก 'stages' ที่สอดคล้องกับ 'lives' ที่เหลืออยู่
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#* for testing
print(f"chosen word \"{chosen_word}\"")
display = []
word_len = len(chosen_word)
for i in range(word_len):
    display.append("_")

lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess letter : ").lower()

    for position in range(word_len):
        letter = chosen_word[position]
        if letter in guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Game over")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("you win")
    
    print(stages[lives])