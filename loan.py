#ASSIGNMENT #4: YOU HAVE BEEN HIRED FINALLY BY THE 21 Century as a Senior Programmer and you've been tasked to help
#in revamping their credit rating system and loan issuing system. Just remember, your job is to make things happen.
#As a Sr. Developer in Python Programming, all the lights and attention are turned towards you and there is a job to be
#done to deliver this critical system on time.

#Your job is to design a simple program to allow the loan officer(s) to enter the customer particulars at the terminal and
#determine if a customer is credit worthy. 

#Based on their looan officer's entry, your system is required to get the best desired resired as shown below in the OUTPUT.

#Please design a program to do the input entry, do the desired calculations and come up with the needed requirements and output them as needed.
#Please consider all the needed variable. If you need to add any, please do add if need is there. Good luck.

import random

CreditScore = random.randrange(400,850)

#Enter the price of the House you wish to Buy
price = int(input("Enter the house price: "))

#Enter the first name
first_name = input("Enter the first name: ")

#Enter the last name
last_name = input("Enter the last name: ")

fullname = first_name + " " + last_name

#Enter the email
email = input("Enter the email address: ")

#Enter the phone number
phone = input("Enter the phone number: ")

#Enter the mailing
address = input("Enter the mailing address: ")

#Enter the mailing
city = input("Enter the City: ")

#Enter the mailing
zipcode = input("Enter the zip code: ")
downPayment = 0

#Qualify for loans with the best interest rates
if CreditScore >= 780:
    status = ("Excellent Credit")
    #print("Zero Down Payment")
    downPayment = (0.10 * price)
    #print ('DownPayment: ' + downPayment)

#Usually qualify for loans with the best interest rates
elif CreditScore >= 740:
    status = ("Very Good")
    downPayment = (0.11 * price)
   # print ('DownPayment: ' + downPayment)

#May face slightly higher loan Interest rates
elif CreditScore >= 720:
    status = ("Above Average")
    downPayment = (0.13 * price)
    #print ('DownPayment: ' + downPayment)

#May qualify for most loans of higher interest rates
elif CreditScore >= 680:
    status = ("Average")
    downPayment = (0.16 * price)
    #print ('DownPayment: ' + downPayment)

#May qualify for most loans at significant higher Interest rates
elif CreditScore >= 620:
    status = ("Below Average")
    downPayment = (0.18 * price)
    #print ('DownPayment: ' + downPayment)

#Usually has some credit issues; will probably not qualify for most loans
elif CreditScore >= 580:
    status = ("Poor Credit Score")
    downPayment = (0.20 * price)
  #print ('DownPayment: ' + downPayment)

#Facing extreme credit issue
elif CreditScore < 520:
    status = ("Poor Credit Score")
    downPayment = (0.25 * price)
    #print ('DownPayment: ' + downPayment)

print('================================================')
print('CUSTOMER DETAILS ARE AS SHOWN BELOW') 
print('================================================')

print('Fullname:' + fullname)
print('Email:' + email)
print('Physical Address:' + address )
print('City:' + city)
print('House Price:' + str(price)) 
print('Down Payment:' + str(downPayment))
print('Credit Score:' + str(CreditScore))
print('Credit Status:' + status) 
