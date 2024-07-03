FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(f"{fahrenheit}F is {celsius}C")

def convert_to_fahrenheit(celsius):
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  print(f"{celsius}C is {fahrenheit}F")

temperature = input("Enter the temperature for conversion: ")

if temperature.isdigit():
  unit = input("Fahrenheit or Celsius, Enter only initial (F, C) ").strip().upper()
  if unit == 'F':
    temperature = int(temperature)
    convert_to_celsius(temperature)
  elif unit == 'C':
    temperature = int(temperature)
    convert_to_fahrenheit(temperature)
  else:
    print("Please enter F for Fahrenheiht and C for Celsius")
else:
  print("Enter a valid integer for the temperature value!!")
