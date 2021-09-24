'''
8.	ให้เขียนโปรแกรมรับข้อมูล 1 บรรทัด ประกอบด้วยตัวเลข 1 หลัก จำนวนไม่เกิน 10 ตัว คั่นด้วยช่องว่าง จากนั้นให้นำตัวเลขที่รับเข้ามาเรียงกัน และหาลำดับการเรียงที่ทำให้มีค่าน้อยที่สุด โดยต้องไม่ขึ้นต้นด้วย 0 เอา 0 ไว้ที่เดิม
Input : 9 4 6 2  คำตอบ 2469, Input : 3 0 8 1 3 3 คำตอบ : 103338
9  7 0   0
3 0 8 1 3 3
3 8 1 3 3
1 3 3 3 8
3 0 8 1 3 3
1 0 3 3 3 8
123560790
30 1 00 2

100023

102003
'''
number_list = []
number_list = [int(e) for e in input("").split()]
number_not_zero = []
if len(number_list) <= 10 and number_list[0] != 0:
    #* select only number not zero
    for number in number_list:
        if number != 0:
            number_not_zero.append(number)
    
    #* sort number
    for num_i in number_not_zero:
        for num_j in range(len(number_not_zero)):
            if num_j+1 >= len(number_not_zero):
                break
            if number_not_zero[num_j] > number_not_zero[num_j+1]:
                number_not_zero[num_j], number_not_zero[num_j+1] = number_not_zero[num_j+1], number_not_zero[num_j]
    
    #* insert value into list that is not zero
    arr_index = 0
    for num_i in range(len(number_list)):
        if number_list[num_i] != 0:
            number_list[num_i] = number_not_zero[arr_index]
            arr_index += 1
    print(number_list)
else:
    print("Please enter number lower than 10")