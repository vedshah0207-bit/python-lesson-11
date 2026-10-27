rows = int(input("Give the amount of rows. "))
half = (rows + 1) // 2

#upper half
for i in range(1, half + 1):
    for j in range(half - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()

#lower half
for i in range(half - 1, 0, -1):
    for j in range(half - i):  #Spacing for the numbers so it is in the center
        print(" ", end="")     #
    for j in range(1, 2 * i):
        print(j, end="")
    print()