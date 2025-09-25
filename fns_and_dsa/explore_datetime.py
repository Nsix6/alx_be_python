from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted)
    return current_date

def calculate_future_date():
    days = int(input("Enter number of days to add to the current date: "))
    today = datetime.now()
    future_date = today + timedelta(days=days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))
    return future_date

display_current_datetime()
calculate_future_date()
