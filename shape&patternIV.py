#author Sila2000

row = int(input("Enter the number of rows: "))
character = input("Enter the character: ")

#upright rt. angle
for i in range(row+1):
    for j in range(i):
        print(character, end=' ')
    print("\r")

print("\n")

#downsided rt.angle
for i in range(row, 0, -1):
    for j in range(i):
        print(character, end=' ')
    print("\r")

print("\n")

#conjugated triangles = upright + downside
for i in range(row+1):
    for j in range(i):
        print(character, end=' ')
    print("\r")
for i in range(row, 0, -1):
    for j in range(i):
        print(character, end=' ')
    print("\r")
