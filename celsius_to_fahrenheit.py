'''
Prints out a conversion table of temperatures from Celsius to Fahrenheit degrees,
the former ranging from 0 to 100 in steps of 10.....
'''

# Insert your code here
min_temperature = 0
max_temperature = 100
step = 10

print('Celsius\tFahrenheit')

for Celsius in range(min_temperature, max_temperature+10, step):
    Fahrenheit = int(Celsius * 9/5) +32

    print(f'{Celsius:7}\t{Fahrenheit:10}')
