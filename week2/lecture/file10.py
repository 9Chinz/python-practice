### ตัวอย่าง เขียนโปรแกรมแสดงสูตรคูณ
### โปรแกรมนี้มี 1 input คือ แม่สูตรคูณ
### Output แสดงแต่ละบรรทัด 4 x   1 = 4

num = int(input("Enter th number of multiplication = "))
# use for loop to iterate 12 times
for i in range(1, 13):
    print(f'{num} x {i:2} = {num*i:3}')