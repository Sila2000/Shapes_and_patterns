#author Sila2000

row = int(input("Enter the number of rows: "))
character = input("Enter the character: ")

#a damn parallelogram
for i in range(row, 0, -1):
    for j in range(i):
        print(" ", end=' ')
    for j in range(row):
        print(character, end=' ')
    print("\r")
