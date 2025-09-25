from datetime import datetime, date, time, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted)

def calculate_future_date():
    days = int(input("Enter number of days to add: "))  
    today = date.today()
    future_date = today + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d %H:%M:%S")
