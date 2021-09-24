flowers = ['Rose','Lily','Tulip','Carnation','Poppy','Sunflower']
print(flowers)

#---------------------------------------------------------------
#* ดูโปรแกรมต่อไปนี้ แล้วบอกความแตกต่างระหว่าง extend กับ append และ +
#---------------------------------------------------------------
flowers.append(['Iris'])
print(flowers)
flowers.extend(['Violet'])
print(flowers)
flowers.append('Jasmine')
print(flowers)
flowers.extend(['Lavender'])
print(flowers)
flowers.append('Jasmine')
print(flowers)

flowers += ['Magnolia']
print(flowers)
flowers += 'Rosemary'
print(flowers)