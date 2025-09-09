# # Example to understand if, elif, and else statements in Python

# number = int(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
# elif number == 0:
#     print("The number is zero.")
# else:
#     print("The number is negative.")

# # Another example with multiple elif
# score = int(input("Enter your score (0-100): "))

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


weather = input("How's the weather today? (sunny/rainy/cloudy): ").lower()

if weather == "sunny":
    activity = input("Do you want to go outside? (yes/no): ").lower()
    if activity == "yes":
        print("Great! Don't forget your sunglasses.")
    elif activity == "no":
        print("Enjoy the sunshine from your window!")
    else:
        print("Hmm, that's an unusual answer!")
elif weather == "rainy":
    umbrella = input("Do you have an umbrella? (yes/no): ").lower()
    if umbrella == "yes":
        print("Perfect! Splash in some puddles.")
    elif umbrella == "no":
        print("Better stay inside and read a book.")
    else:
        print("Not sure what to do without an answer!")
elif weather == "cloudy":
    mood = input("Are you feeling sleepy? (yes/no): ").lower()
    if mood == "yes":
        print("A nap sounds perfect for a cloudy day.")
    elif mood == "no":
        print("Maybe go for a walk and enjoy the cool air.")
    else:
        print("Can't decide? Just relax!")
else:
    print("I can't predict that kind of weather!")