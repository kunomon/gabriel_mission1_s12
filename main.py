from measurement_converter import MeasurementConverter

print('''
[1]. Centimeters to Meters
''')

choice = input('Choose an option: ')
value = float(input('Type a value: '))

if choice == '1':
    result = MeasurementConverter.centimeters_to_meters(value)
    
print('Result:', result)