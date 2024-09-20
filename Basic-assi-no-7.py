# Minimum requirements for Army Test
mini_age: int = 18  # Minimum age requirement
mini_qualification: list[str] = ["inter", "matric"]  # Acceptable qualifications
mini_height: float = 5.10  # Minimum height in feet

# Input for age, qualification, and height
age: int = int(input("Enter your age: "))
qualification: str = input("Enter your Qualification (inter/matric): ").lower()
height: float = float(input("Enter your height in feet: "))

# Check if age meets the minimum requirement
if age >= mini_age:
    print("Your age is 18+ you are Pass.") 
    
    # Check if qualification is one of the acceptable options
    if qualification in mini_qualification:
        print("Your Qualification is inter or matric, you are Pass.")
        
        # Check if height meets the minimum requirement
        if height >= mini_height:     
            print("Your height is 5.10 or above, you are Pass.")
        else:
            print("Your height is below 5.10, you are Fail.")    
    else:
        print("Your Qualification is not inter or matric, you are Fail.")        
else:
    print("Your age is below 18, you are Fail.")    
