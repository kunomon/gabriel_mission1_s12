from measurement_converter import MeasurementConverter

print('''
[1]. Centimeters to Meters
[2]. Meters to Centimeters
''')

choice = input('Choose an option: ')
value = float(input('Type a value: '))

if choice == '1':
    result = MeasurementConverter.centimeters_to_meters(value)
elif choice == '2':
    result = MeasurementConverter.meters_to_centimeters(value)
    
print('Result:', result)