#---------------------------------------------------
#* ในสมัยโรมัน มีการส่งข้อมูลแบบเข้ารหัส เพื่อป้องกันการอ่านแอบอ่าน
#* เรียกว่าการเข้ารหัสแบบซีซาร์ โดยใช้วิธีการเลื่อนตัวอักษร
#* abcdefghijklmnopqrstuvwxyz
#* เช่น ถ้ากำหนดเลื่อน 5 ข้อความ hello -> mkrru
#* กรณีที่เป็นตัว z จะวนกลับไปใช้ abc ใหม่
#---------------------------------------------------

#| Ex 5.7 จากโปรแกรมต่อไปนี้ จงเขียนโปรแกรมในจุดที่ระบุ TODO 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount):    
#     cipher_text = ''
#     for char in plain_text:
#         position = alphabet.index(char)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]

#     print(cipher_text)

# def decrypt(cipher_text, shift_amount):
#     plain_text = ''
#     for char in cipher_text:
#         position = alphabet.index(char)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
    
#     print(plain_text)

def ceasar(text, shift_amount, cipher_direction):
    new_text = ''
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        new_text += alphabet[new_position]

    print(new_text)

ceasar("hello", 5, "encode")