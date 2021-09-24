"""
4.	ให้เขียนโปรแกรมค้นหาว่ามีข้อความ KMITL (เรียงติดกัน) บนตารางที่กำหนดให้กี่คำ พร้อมแสดงตำแหน่งของทุกตัวอักษรที่ประกอบกันเป็นข้อความ KMITL ของทุกคำ  
นักศึกษาสามารถกำหนดค่าเริ่มต้นของตารางได้ดังนี้
"""
string_container = []

#*                  ROW   0    1    2    3    4    COLUMN
string_container.append(['*', '*', '*', '*', '*']) #* 0
string_container.append(['*', 'M', 'M', '*', '*']) #* 1
string_container.append(['*', 'K', 'I', 'K', '*']) #* 2
string_container.append(['*', 'I', 'T', '*', '*']) #* 3
string_container.append(['*', '*', 'L', '*', '*']) #* 4

def draw_table():
    print(f"ROW/COL  {'1':^4} {'2':^4} {'3':^4} {'4':^4} {'5':^4}")
    for row in range(len(string_container)):
        print(f" {row+1:^5}{'':<2}{string_container[row]}")
    print("\n")

def search_around(current_row, current_column, char_finding):
    return_list = []
    for row in range(-1, 2):
        for col in range(-1, 2):
            if (string_container[current_row+row][current_column+col] == char_finding):
                return_list.append(f"{current_row+row}{current_column+col}")
    return return_list

k_list = []
result_list = []

for row in range(len(string_container)):
    for column in range(len(string_container[row])):
        if string_container[row][column] == "K":
            k_list.append(f"{row}{column}")

for k in k_list:
    current_row = int(k[0])
    current_column = int(k[1])
    m_list = search_around(current_row, current_column, "M")

    for m in m_list:
        current_row = int(m[0])
        current_column = int(m[1])
        i_list = search_around(current_row, current_column, "I")

        for i in i_list:
            current_row = int(i[0])
            current_column = int(i[1])
            t_list = search_around(current_row, current_column, "T")

            for t in t_list:
                current_row = int(t[0])
                current_column = int(t[1])
                for row in range(-1, 2):
                    for col in range(-1, 2):
                        if (string_container[current_row+row][current_column+col] == "L"):
                            result_list.append(f"K{int(k[0])+1}{int(k[1])+1} M{int(m[0])+1}{int(m[1])+1} I{int(i[0])+1}{int(i[1])+1} T{int(t[0])+1}{int(t[1])+1} L{current_row+row+1}{current_column+col+1}")

draw_table()

for item in result_list:
    print(item)
print(f"KMITL Count = {len(result_list)}")