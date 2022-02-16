# Program Python untuk mengubah suhu dalam celsius ke fahrenheit

# celsius ke fahrenheit 
celsius = float(input("Masukan parameter celcius: "))

fahrenheit = (celsius * 1.8) + 32
print('%0.1f derajat Celsius sama dengan %0.1f derajat Fahrenheit' %(celsius,fahrenheit))

# fahrenheit
fahrenheit = float(input("Masukan parameter fahrenheit: "))

celsius = (fahrenheit - 32) / 1.8
print('%0.1f derajat Fahrenheit sama dengan %0.1f derajat Celsius' %(fahrenheit,celsius))