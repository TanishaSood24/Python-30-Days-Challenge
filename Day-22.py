import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
def celsius_to_kelvin(c):
    return c + 273.15
def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Setup argparse
parser = argparse.ArgumentParser(description="🌡️ Temperature Converter CLI Tool")
parser.add_argument('--value', type=float, required=True, help="Temperature value to convert")
parser.add_argument('--from_unit', type=str, required=True, choices=['celsius', 'fahrenheit', 'kelvin'], help="Source unit")
parser.add_argument('--to_unit', type=str, required=True, choices=['celsius', 'fahrenheit', 'kelvin'], help="Target unit")

args = parser.parse_args()

value = args.value
from_unit = args.from_unit.lower()
to_unit = args.to_unit.lower()

# Conversion logic
converted = None

if from_unit == to_unit:
    converted = value
elif from_unit == 'celsius':
    converted = celsius_to_fahrenheit(value) if to_unit == 'fahrenheit' else celsius_to_kelvin(value)
elif from_unit == 'fahrenheit':
    converted = fahrenheit_to_celsius(value) if to_unit == 'celsius' else fahrenheit_to_kelvin(value)
elif from_unit == 'kelvin':
    converted = kelvin_to_celsius(value) if to_unit == 'celsius' else kelvin_to_fahrenheit(value)

# Print result
symbols = {'celsius': '°C', 'fahrenheit': '°F', 'kelvin': 'K'}
print(f"{value}{symbols[from_unit]} is {round(converted, 2)}{symbols[to_unit]}")
