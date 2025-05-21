import random

print(random.randint(3, 9))


coin_toss = ["heads", "tails"]
print(random.choice(coin_toss))




# Meal Recommendation System
#
# Create a program that recommends what to eat based on the time of day.
# The program will:
# 1. Ask the user for the current time (in hours, using 24-hour format)
# 2. Recommend a meal or snack based on the time
# 3. Add a friendly message with the recommendation



# Instructions for students:
# 1. Ask the user for the current time in hours (0-23)
# 2. Convert the input to an integer
# 3. Use if-elif-else to recommend different meals based on time ranges
# 4. Include a default option for unusual times

time = int(input("What is the time? "))

if  7<= time <=10 :
    print(f"it's {time}am, have a sandwich.")
elif 10 <= time <=15 :
    print(f"it's {time}, have some salmon for lunch.")
elif 15 <= time <=19 :
    print(f"it's {time}, have pizza for dinner")
elif 20 <= time <=24 :
    print(f"it's {time}pm, have a snack")
elif 0 <= time <= 7:
    print("it's night time, go to sleep")
else:
    print("This is not a correct time")