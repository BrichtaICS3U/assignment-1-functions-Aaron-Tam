# Assignment 1
# ICS3U
# <Aaron T>
# March 28, 2018

import math

def CtoF (C):
    F = (1.8) * C + 32
    return F

def FtoC (F):
    C = 5/9 * (F - 32)
    return C

#print temperature = int(input('Enter your temperature in Celsius: '))
print ('Enter 1 to convert a temperature to Celsius and Enter 2 to convert a temperature to Farenheit')
choice = int(input())
temperature = int(input('Now enter your temperature. '))
if choice == 1 and temperature >= -273.15:
    print (CtoF(temperature))
    print ('If you want to continue this program, enter yes, if not, enter no.')
    
elif choice == 2 and temperature >= -459.67:
    print (FtoC(temperature))
else:
    print ('Please choose either 1 or 2.')
    
      
            








