from measurement_converter import MeasurementConverter
from temperature_converter import TemperatureConverter

print('''
[1]. Centimeters to Meters
[2]. Meters to Centimeters
[3]. Celsius to Fahrenheit
[4]. Fahrenheit to Celsius
''')

choice = input('Choose an option: ')
value = float(input('Type a value: '))

if choice == '1':
    result = MeasurementConverter.centimeters_to_meters(value)
elif choice == '2':
    result = MeasurementConverter.meters_to_centimeters(value)
elif choice == '3':
    result = TemperatureConverter.celsius_to_fahrenheit(value)
else:
    result = TemperatureConverter.fahrenheit_to_celsius(value)
    
print('Result:', result)