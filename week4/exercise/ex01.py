
while True:
    n = int(input("Enter n : (0-9): "))
    if n in range(0, 10):
        break
    else:
        print("Please enter number between 0 and 9! :")

for i in range(0,n+1):
    for j in range(0, n+1):
        if i <= j:
            print(i, end='')
        else:
            print(j, end='')
    for k in range(n-1, -1, -1):
        if i <= k:
            print(i, end="")
        else:
            print(k, end="")
    print("")
for i in range(n-1, -1, -1):
    for j in range(0, n+1):
        if i >= j:
            print(j, end="")
        else:
            print(i, end="")
    for k in range(n-1, -1, -1):
        if i >= k:
            print(k, end="")
        else:
            print(i, end="")
    print("")