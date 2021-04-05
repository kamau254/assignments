#Enter Full Names
fname = input("Enter First Name:") #First Name
lname = input("Enter Last Name:") #last Name
fullnames = fname + " " + lname

#Enter phone, email
phone = input("Enter Customer's Phone Number:")
email = input("Enter Customer's email address:")

#price of a used car
price = 10000
has_good_credit = True;

if has_good_credit:
    down_payment = (price * 0.1)
else:
    down_payment = (0.2 * price)

print('==================================================================')
print("Full Names:" + fullnames)
print("Phone: " + phone)
print("Email: " + email)
print("Down Payment: " + str(down_payment))




# This below: Is the Expected output:

# Full Names: Benard Njoroge Otieno
# Phone: 872-098-9876
# Email: UsedCarSalesman@gmail.com
# Down Payment:  1000.00