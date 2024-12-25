def cilsius_to_farenheit(cilsius):
    return cilsius * 1.8 + 32

farenheit = float(input("Enter Degrees Fahrenheit:"))

Result = cilsius_to_farenheit(farenheit)

print(f"{farenheit} degrees Fahrenheit becomes {Result} degrees Celsius.")