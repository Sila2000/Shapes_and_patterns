#author Sila2000

row = int(input("Enter the number of rows: "))
character = input("Enter the character: ")

#a damn rectangle
for i in range(row):
    for j in range(row):
        print(character, end=' ')
    print("\r")
