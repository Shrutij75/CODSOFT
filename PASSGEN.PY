#1.Desired length is taken from the user
#2.generate a password
#3.display the password to the user

import random
import string
no=int(input("Enter the length of the password user needed::::"))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
sym=string.punctuation

all=lower+upper+num+sym
temp=random.sample(all,no)
passwrd="".join(temp)
print("the generated password is:",passwrd)