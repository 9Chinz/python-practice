#| Ex.3.3 ให้เขียนโปรแกรมแสดงตารางเทียบอุณหภูมิระหว่าง C กับ F
#|        F= C/5*9+32

print (" c : f")
for temp_c in range(0, 41):
    temp_f = temp_c/5*9+32
    print(f"{temp_c:2} = {temp_f:.2f}")