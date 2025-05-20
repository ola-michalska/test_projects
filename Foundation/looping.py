#looping
'''
for loop: starts with *for*

for char in "Ola":
    print(char)

*char* is an arbitrary value - whatever i want to call it
loop over the string, assign each letter in it to the variable "char"

can loop: string,

CAN'T loop int - must use range, not inclusive (so 5=4) also starts from 0

'''


for char in "Ola":
    print(char)

for num in range(4):
    print(num)

for person in ["Sam", "Sally", "Bob", "Jess"]:
    print(person)



#list
'''
must have a square bracket
any valid data type
'''


fav_food = ["Pizza", "Lasagna", "Tacos"]

for food in fav_food:
    print(f"I like {food}")


#while loop
'''

'''

store_capacity = 10

while store_capacity > 0:
    print("Spaces available: ", store_capacity)
    store_capacity -= 1

print("\n please wait for someone to leave")



