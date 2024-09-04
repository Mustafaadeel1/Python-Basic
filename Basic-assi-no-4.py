#Question no 1: String is not change able :So we can change string value:
#String change into List: To check the type : We can use type() function.

name = "My name is Mustafa"
list_1 = list(name)
print(type(list_1))

laptop = "lenovo thinkpad"
list_2 = list(laptop)
print(type(list_2))

city = "My city is sialkot"
list_3 = list(city)
print(list_3)

#String change into tuple:

name = "My name is Mustafa"
tuple_1 =tuple(name)
print(type(tuple_1))

laptop = "lenovo thinkpad"
tuple_2= tuple(laptop)
print(type(tuple_2))

city = "My city is sialkot"
tuple_3= tuple(city)
print(tuple_3)

#String change into set:

name = "My name is Mustafa"
set_1 =set(name)
print(type(set_1))

laptop = "lenovo thinkpad"
set_2= set(laptop)
print(type(set_2))

city = "My city is sialkot"
set_3= set(city)
print(set_3)

#Question no 2:escape sequence "\name"\

agi = "\"Sir Zia\" said: \nIf you want to learn AGI, it will drive you crazy."
print(agi)

cricket = "\"Virat Kholi\": \nis the best better in the world."
print(cricket)

islam ="\"Prophet Muhmmad(s.a.w)\": \nIs the best man in the world."
print(islam)