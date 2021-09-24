# ---------------------------------------------------------------
# * การลบข้อมูลใน List ทำได้หลายวิธี
# *      clear เป็นการลบ list ทั้งหมด
# *      remove เป็นการลบโดยอ้างถึงค่า
# *      del เป็นการลบโดยอ้างถึงตำแหน่ง
# *      pop เป็นการลบโดยอ้างถึงตำแหน่ง
# ---------------------------------------------------------------

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

print(motorcycles)
del motorcycles[2]
print(motorcycles)
motorcycles.pop(0)
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles.clear()
print(motorcycles)