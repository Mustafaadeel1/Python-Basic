# Using for create Table of "2":
i =2
for x in range(1,10+1):
    print(f"{i} X {x} = {i*x}")
print()    
# Using for create Table of "3":    
i =3
for x in range(1,10+1):
    print(f"{i} X {x} = {i*x}")
print()
# Using for create Table of "4":
i = 4
for x in range(1,10+1):
    print(f"{i} X {x} = {i*x}")        
print()
# Using for create Table of "5":
i = 5
for x in range(1,10+1):
    print(f"{i} X {x} = {i*x}")        
print()
# Using for create Table of "6":
i = 6
for x in range(1,10+1):
    print(f"{i} X {x} = {i*x}")        
print()
# Using for create Table of "7":
i = 7
for x in range(1,10+1):
    print(f"{i} X {x} = {i*x}")        
print()
# Using for create Table of "8":
i = 8
for x in range(1,10+1):
    print(f"{i} X {x} = {i*x}")  
print()
# Using for create Table of "9":
i = 9
for x in range(1,10+1):
    print(f"{i} X {x} = {i*x}") 
print() 

# Using for create Table of "10":
i = 10
for x in range(1,10+1):
    print(f"{i} X {x} = {i*x}")
print()  

# This is Nested Loop: Mean "loop in another loop"
# 1. In Design we draw Aesthetics: ****
for y in range(1,3):
    for i in range(1,3):
        print("****")
        if i == 2:
            break
print()    

#2 Number of rows
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
 