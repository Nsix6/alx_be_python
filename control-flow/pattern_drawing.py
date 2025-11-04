size = int(input("Enter the size of the pattern: ").strip())

for i in range(size):
    for j in range(size):
        print("*", end="")
    print()