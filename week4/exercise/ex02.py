
while True:
    n = int(input("Enter n : (0-9): "))
    if n in range(0, 10):
        break
    else:
        print("Please enter number between 0 and 9! :")

for i in range(0, n+1):
    for s in range(0, n-i):
        print(" ", end="")
    for j in range(0, i+1):
        print(j, end="")
    for k in range(i-1, -1, -1):
        print(k, end="")
    print("")
for i in range(0, n):
    for s in range(0, i+1):
        print(" ", end="")
    for j in range(0, n-i):
        print(j, end="")
    for k in range(n-i-2, -1, -1):
        print(k, end="")
    print("")