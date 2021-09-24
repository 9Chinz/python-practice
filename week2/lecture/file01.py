flowers = ['Rose', 'Lily', 'Tulip', 'Carnation', 'Poppy', 'Sunflower']
print(flowers)

# ---------------------------------------------------------------
# * ดูโปรแกรมต่อไปนี้ แล้วบอกความแตกต่างระหว่าง extend กับ append และ +
# ---------------------------------------------------------------
flowers.append(['Iris'])
print(flowers)
flowers.extend(['Violet'])
print(flowers)
flowers.append('Jasmine')
print(flowers)
flowers.extend(['Lavender']) # เอา list lavender รวมกับ list flowers
print(flowers)
flowers.append('Jasmine') # เอา Jasmine ต่อถ้ายใน List flowers
print(flowers)

flowers += ['Magnolia'] # list + list ได้ list ตัวใหม่ ที่เอาสามาชิก 2 list ไปเป็นสมาชิกตัวใหม่
print(flowers)
flowers += 'Rosemary' # แยกออกไปตัวๆ => 'R', 'o', 's', 'e', 'm', 'a', 'r', 'y' เพราะ string เหมือนเป็น list อยู่แล้ว
print(flowers)