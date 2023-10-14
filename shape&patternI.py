row = int(input("Enter the number of rows: "))
character = input("Enter character: ")

#horizontal line of characters
print(character*row)

print("\n")

#vertical line of characters
for i in range(row):
    print(character)
