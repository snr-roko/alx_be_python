task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
  case "high":
    if time_bound == "yes":
      print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    elif time_bound == "no":
      print(f"Reminder: '{task}' is a {priority} priority task that requires attention as soon as possible!")
  case "medium":
      if time_bound == "yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention\n If there is work to do; Delegate!")
      elif time_bound == "no":
        print(f"Reminder: '{task}' is a {priority} priority task. Schedule for it to be done!")
  case "low":
    if time_bound == "yes":
      print(f"Reminder: '{task}' is a {priority} priority task. Delegate")
    elif time_bound == "no":
      print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")