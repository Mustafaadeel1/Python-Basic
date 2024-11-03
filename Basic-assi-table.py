
user=int(input("Enter a number which you like table: "))
for x in range(1,10+1):
    print(f"{user} X {x} = {user**x}")
print() 


for i in range(1,5):
    print("*****")



for num in range(1, 101):  
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")  
    elif num % 3 == 0:
        print("Fizz")  
    elif num % 5 == 0:
        print("Buzz")  
    else:
        print(num)  
