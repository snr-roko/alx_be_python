FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(f"{fahrenheit}F is {celsius}C")

def convert_to_fahrenheit(celsius):
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  print(f"{celsius}C is {fahrenheit}F")

temperature = input("Enter the temperature to convert: ")

if temperature.isdigit():
  unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
  if unit == 'F':
    temperature = int(temperature)
    convert_to_celsius(temperature)
  elif unit == 'C':
    temperature = int(temperature)
    convert_to_fahrenheit(temperature)
  else:
    print("Please enter F for Fahrenheiht and C for Celsius")
else:
  print("Invalid temperature. Please enter a numeric value.")
