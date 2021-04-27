def Fahrenheit_Celsius(temp, state):
    if state == 0:
        fahrenheit = ((temp * (9/5)) + 32)
        print('Fahrenheit Temperature:' + str(fahrenheit))
        print('Celcius Temperature:' + str(temp))
    else:
        celcius = ((temp - 32)  *(5/9))
        print('Celcius Temperature:' + str(celcius))
        print('Fahrenheit Temperature:' + str(temp))
    
def printOptions():
    print("""Options: 
    [C] Convert from Celcius 
    [F] Convert from Fahreheit 
    [M] Convert from Miles 
    [KM] Convert from Kilometers 
    [IN] Convert from Inches  
    [CM] Convert from Centimeters 
    [Q] Quit 
    \n""")

def toka():
    print('-----------------{ EXIT }----------------')
    exit('Thank you for using our system. Au Revoir!')

def lastOptions():
    print("""Options: 
    [P] Print Options  
    [Q] Quit \n""")

    option = input('Choose an option: ')
    print('------------{ END }------------')

    user_option = option.upper()

    if user_option == 'P':
        printOptions()
    elif user_option == 'Q':
        toka()


def kilometers_miles(distance, state):
    if state == 0:
        kilometers = (distance * 1.6)
        print('Kilometers Distance:' + str(kilometers))
        print('Miles Distance:' + str(distance))
    else:
        miles = (distance / 1.6)
        print('Miles Distance:' + str(miles))
        print('Kilometers Distance:' + str(distance))

def centimeters_meters(length):
    
    
    centimeters = (length * 100)
    meters = (length / 100)

def yards_meters(yard):
   yards = (yard * 1.094)
   meters = (yard / 1.094)

def inches_centimeters(centi, state):
    if state == 0:
        inches = (centi / 2.54)
        print('Inches:' + str(inches))
        print('Centimeters:' + str(centi))
    else:
        centimeters = (centi * 2.54)
        print('Centimeters:' + str(centimeters))
        print('Inches:' + str(centi))
    
    
printOptions()
user_option ='A'


while user_option != 'Q':
    option = input('Choose one the above options: ')
    user_option = option.upper()
    
    data = input('Enter the number to convert: ')
    user_input = int(data)
    print(user_option)

    if user_option == 'C': 
        Fahrenheit_Celsius( user_input, 1)   

    elif user_option == 'F':
        Fahrenheit_Celsius( user_input ,0)

    elif user_option == 'M':
        kilometers_miles(user_input , 1)    

    elif user_option == 'KM':
        kilometers_miles(user_input , 0)    

    elif user_option == 'IN':
        inches_centimeters(user_input , 0)  
        
    elif user_option == 'CM':
        inches_centimeters(user_input , 1)  
    elif user_option == 'Q':
        toka()

    else:
        exit('Invalid Option')
    
    lastOptions()

toka()
