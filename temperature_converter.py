class TemperatureConverter:
    def __init__():
        pass

    def celsius_to_fahrenheit(celsius_value):
        return celsius_value * (9/5) + 32

    def fahrenheit_to_celsius(fah_value):
        return (fah_value - 32) / (9/5)

# Testing Area
result = TemperatureConverter.fahrenheit_to_celsius(32)
print('Result:', result)