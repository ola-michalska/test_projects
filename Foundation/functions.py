#functions
'''

reusable piece of code

def - define function,
function in python denoted by ()

have to be called/invoced!!

return makes the function do something

'''

name = input("What is your name? ")
def say_hello(name):
    print("hello! ", name)
    print("hello again!")
say_hello(name)




def say_name(other_name):
    print(f"Hello! Nice to meet you {other_name}!")
say_name(input("What is your name? "))



def say_hi(third_name, location):
    return f"Hello, {third_name}! You are at {location}."
print(say_hi("Bob", "London"))

