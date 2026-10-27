print("Half pyramid of stars")
n = int(input("Give the numbers of rows in the half pyramid. "))

for i in range(n): #Outer loop to handle numbers of rows
    for j in range(i + 1): #Inner loop to handle number of columns
        print("* ", end="") #end is to make sure it skip line
    print() # this is to add line to make a 2d shape