firstname = input('Enter your first name:')
lastname = input('Enter your last name:')
fullname = firstname + " " + lastname
country = input('Enter your country of origin:')
profession = input('Enter your current job:')
email = firstname + lastname + '@' + firstname.lower() + lastname.lower() + '.com'
phone = input('Enter your phone number with the country code:')
city = input('Enter your city of residence:')
address = input('Enter your Address:')

print('*********************************************************************')

print('Name: ' + fullname)
print('Country: ' + country)
print('Profession: ' + profession)
print('Email: ' + email)
print('Phone: ' + phone)
print('City: ' + city)
print('Address: ' + address)

print('*********************************************************************')