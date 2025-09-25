FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


userGuess = int(input("Enter the temprature to convert: "))
if userGuess != int:
    print("Invalid temprature. Please enter a numeric value.")
    exit()
unit = input("Is this temprature in Celsius or Fahrenheit? (C/F): ").strip().upper()
if unit == 'C':
    converted = convert_to_fahrenheit(userGuess)
    print(f"{userGuess}°C is {converted:.2f}°F")
elif unit == 'F':
    converted = convert_to_celsius(userGuess)
    print(f"{userGuess}°F is {converted:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")