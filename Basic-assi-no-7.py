# Army test minimum requirement: 
mini_age: int = 18
mini_Qualification: str = ("2nd year")
mini_hight : float = 5.10
age = int(input("Enter your age: "))
qualification = input("Enter your Qualification (e.g., '2nd year'): ")
height = float(input("Enter your height in feet: "))

if age >= mini_age:
    print("Your age is 18+ you are Pass.") 
    if qualification== mini_Qualification:
        print("Your Qualification 2nd above your are Pass.")
        if height >=mini_hight:     
            print("Your hight is above 5.10 you are Pass.")
        else:
            print("Your hight is not above 5.10 you are Fail.")    
    else:
        print("Your Qualification is not 2nd above your are Fail.")        
else:
    print("Your age is not 18+ you are Fail.")    
