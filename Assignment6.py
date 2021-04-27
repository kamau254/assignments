def remarks():
    if region == 'A' and gender == 'M':
        if average >= 80:
            print('CONGRATULATIONS ' + fullnames + ', YOU HAVE EARNED THE FULL SCHOLARSHIP!!')
        else:
            print('WE ARE SORRY TO INFORM YOU THAT YOU WERE NOT ABLE TO QUALIFY FOR THE SCHOLARSHIP.') 
    
    elif region == 'A' and gender == 'F':
        if average >= 76:
            print('CONGRATULATIONS ' + fullnames + ', YOU HAVE EARNED THE FULL SCHOLARSHIP!!')

        else:
            print('WE ARE SORRY TO INFORM YOU THAT YOU WERE NOT ABLE TO QUALIFY FOR THE SCHOLARSHIP.') 


    elif region == 'O' and gender == 'M':
        if average >= 80:
            print('CONGRATULATIONS ' + fullnames + ', YOU HAVE EARNED THE HALF SCHOLARSHIP!!')

        else:
            print('WE ARE SORRY TO INFORM YOU THAT YOU WERE NOT ABLE TO QUALIFY FOR THE SCHOLARSHIP.') 


    elif region == 'O' and gender == 'F':
        if average >= 80:
            print('CONGRATULATIONS ' + fullnames + ', YOU HAVE EARNED THE FULL SCHOLARSHIP!!')

        else:
            print('WE ARE SORRY TO INFORM YOU THAT YOU WERE NOT ABLE TO QUALIFY FOR THE SCHOLARSHIP.')
    else:
        print('Sorry Invalid details.')



print('ENTER THE TRUE AND CORRECT DETAILS OR ELSE YOU WILL BE DISQUALIFIED AUTOMATICALLY')
print('')
print('-----------------------{ PERSIONAL DETAILS }------------------------')

fname = input('Enter your first name: ')
lname = input('Enter your last name: ')
gender1 = input('Enter M/F: ')
email = input('Enter a valid email: ')
phone = input('Enter your phone number. Ensure that it has your country code: ')

print('')
print('-----------------------{ GEOGRAPHIC DETAILS }------------------------')

mail_address = input('Enter your mailing address: ')
city = input('Enter your city: ')
country = input('Enter your country: ')
region1 = input('For Africa, press A. For other regions, press O: ')

print('')
print('-----------------------{ EXAMINATION DETAILS }------------------------')

quiz = input('Enter your score for quiz: ')
quiz2 = input('Enter your score for quiz2: ')
quiz3 = input('Enter your score for quiz3: ')
test1 = input('Enter your score for test1: ')
test2 = input('Enter your score for test2: ')
zoom_scores = input('Enter your score for zoom calls: ')
programming_assignments = input('Enter your score for programming assingments: ')

print('')
print('... PROSSESING')

region = region1.upper()
gender = gender1.upper()
fullnames = fname + lname
average = ((int(quiz) + int(quiz2) + int(quiz3) + int(test1) + int(test2))/5)

print('')
print('-----------------------{ DETAILED REPORT }------------------------')

print('FULLNAME: ' + fullnames)
print('EMAIL: ' + email)
print('PHONE: ' + phone)
print('GENDER: ' + gender)
print('')

print('REGION: ' + region)
print('COUNTRY: ' + country)
print('CITY: ' + city)
print('')

print('SCORE AVERAGE: ' + str(average))
print('ZOOM CALLS: ' + zoom_scores)
print('H/W PROGRAMMING ASSIGNMENTS: ' + programming_assignments)

remarks()


