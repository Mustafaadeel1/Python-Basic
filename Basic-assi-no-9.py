#Taking square in list value:"without using square function"
def num_list():
    square: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = [num * 2 for num in square]
    print(new_list)

num_list() 

#Add all value in list: "Without using sum function"
def add_list():
    add_num: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    total = 0
    for num in add_num:
        total +=num
    print(total)

add_list()
 
#Reverse all value:
def reverse_list():
    rev_list: list = [1,2,3,4,5,6,7,8,9,10]
    rev_2 = rev_list[::-1]
    print(rev_2)
reverse_list()    