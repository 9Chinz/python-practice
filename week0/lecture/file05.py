## ห้ามใช้ == กับ float
#* เรื่องชวนงงกับเลขทศนิยม
#* https://docs.python.org/3/tutorial/floatingpoint.html

Income = float(input("Enter your income (Baht): "))
VAT = float(input("Enter your VAT (%): "))
Tax = Income * VAT / 100
print("Your Tax is ", Tax, "Baht")