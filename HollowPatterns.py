rows = 5

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == 1 or i == rows or j == 1 or j == rows or i == j or rows+1-i == j or i == ((rows+1)//2) or j == ((rows+1)//2):
            print("*", end =" ")
        else:
            print(" ", end = " ")
    print()
        



rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if i == rows or j == 1 or i == j:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()





rows = 5

for i in range(1, rows + 1):
    k = 1
    for j in range(1, i + 1):
        if i == rows or j == 1 or i == j:
            print(k, end = " ")
        else:
            print(" ", end = " ")
        k+=1
    print()
    
    
    
    
    
rows = 5

for i in range(1, rows + 1):
    k = rows
    for j in range(1, i + 1):
        if i == rows or j == 1 or i == j:
            print(k, end = " ")
        else:
            print(" ", end = " ")
        k-=1
    print()



print()
print()



rows = 5

for i in range(1, rows + 1):
    k = rows
    for j in range(1, rows + 1):
        if i == 1:
            print(k, end=" ")
        elif j == i:
            print(5, end=" ")
        elif j == rows:
            print(i, end=" ")
        else:
            print(" ", end=" ")
        k -= 1
    print()
    

    


