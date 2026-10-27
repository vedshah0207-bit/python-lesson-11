rows = int(input("Enter the amount of rows to make. "))
num = 1

for i in range(rows):
    for j in range(i + 1):
        print(num, end=" ")
        num = num + 1
    print()


# 4 in input.
# T4 = 10

#1
#2 3
#4 5 6 
#7 8 9 10
#
#n = Tn