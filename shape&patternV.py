#author Sila2000

row = int(input("Enter the number of row: "))

#a triangle
for i in range(row):
    for j in range(row - i, -1, -1):
        print(" ", end='')
    for j in range(i + 1):
        print("*", end=' ')
    print("\r")
