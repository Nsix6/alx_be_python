#!/usr/bin/env python3

user_guess = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

if user_guess == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_guess == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user_guess == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")