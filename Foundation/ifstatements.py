#conditional programming

'''

= assignment operator

Comparison operators / Comparitive operators:
== equal to
!= not equal
> greater than
< less than
>= greater than or equal to
<= less than or equal to

ALWAYS RESULTS IN A BOOLEAN VALUE true/false



'''


#simple true/false

light_color = "green"

if light_color == "green":
    print('go')

if light_color == "red":
    print('stop')

# Comparison operator
temperature = 26

print(temperature > 30) #will print FALSE



#LOGICAL OPERATORS:
'''
and - both have to be true
not - first one true second one false
or - at least one true
'''

is_sunny = True

go_to_the_beach = (temperature > 25) and is_sunny # TRUE and TRUE
print("Should I go to the beach?", go_to_the_beach) #will print True



# if/else

if (temperature > 25) and is_sunny:
    print("Go to the beach")
else:
    print("go back home")





age = int(input("How old are you? "))

if age >= 13:
    print(f"You are {age} years old, you can watch the movie")
else:
    print(f"You are not yet old enough to watch the movie")

#elif

# Weather Activity Recommender
#
# Create a program that:
# 1. Asks the user for today's weather (sunny, rainy, or snowy)
# 2. Uses if-else to recommend an appropriate activity
# 3. Tells the user to have a great day
#
# This provides a practical, relatable example for if-else statements.
# """
#
# # Instructions for students:
# # 1. Ask the user for the current weather
# # 2. Based on their input, recommend a suitable activity
# # 3. Handle invalid inputs with a default message


today_weather = input("What is the weather like today? Is it sunny, snowy, or rainy? ").lower() #.lower is a string method changes the capitalisation to lower case (defensive programming)

if today_weather == "sunny":
    print("Go swimming")
elif today_weather == "rainy":
    print("go to a cafe")
elif today_weather == "snowy":
    print("read by the fire")
else:
    print("sorry I don't understand.")



print("Have a great day!")
