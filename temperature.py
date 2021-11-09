def convert(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Enter a temperature in degrees Celsius: "))
result = convert(celsius)
print(str(celsius) + " degrees celsius are " + str(result) + " degrees farenheit")
