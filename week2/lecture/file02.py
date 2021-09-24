# ---------------------------------------------------------------
# * การแก้ไขข้อมูลตัวใดตัวหนึ่งใน list ทำได้โดยระบุตำแหน่งและกำหนดข้อมูลใหม่
# ---------------------------------------------------------------

list1 = ['physics', 'chemistry', 'calculus', 'biology'];
print("Old value available at index 2 : ", list1[2])
list1[2] = 'programming';
print("New value available at index 2 : ", list1[2])
print(list1)

# ---------------------------------------------------------------
# * การแทรกข้อมูลใน List จะใช้ insert โดยระบุตำแหน่งที่ insert
# ---------------------------------------------------------------

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
