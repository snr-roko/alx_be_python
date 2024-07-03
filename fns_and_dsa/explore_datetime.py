from datetime import datetime
from datetime import date
from datetime import timedelta

def display_current_datetime():
  now = datetime.now()
  formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
  print(formatted_date)


def calculate_future_date():
  days = input("Lets go into the future \nEnter the number of days ")
  today = date.today()
  if days.isdigit():
    days = int(days)
    delta = timedelta(days = days)
    future_date = today + delta
    print(future_date.strftime("%Y-%m-%d"))
  else:
    print("Please Enter a valid integer as number of days")

calculate_future_date()