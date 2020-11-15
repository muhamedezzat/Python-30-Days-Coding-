import random
import string

'''

here we define variables that contain all characters which password is made from it.
it must be a string type not digits.
we can define varibles as a list contains words to generate password from this words

we can use string library insted of define varibles as 
The constants defined in this module are:

string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants described below. 

string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. 

string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. 

string.digits
The string '0123456789'.

string.hexdigits
The string '0123456789abcdefABCDEF'.

string.octdigits
The string '01234567'.

string.punctuation
String of ASCII characters which are considered punctuation characters 
in the C locale: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.

string.printable
String of ASCII characters which are considered printable. 
This is a combination of digits, ascii_letters, punctuation, and whitespace.

string.whitespace
A string containing all ASCII characters that are considered whitespace. 
This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.

'''
uppString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowString = uppString.lower()
numbers = "0123456789"
specialChar = "@#&*^!"
allPassword = f"{uppString}{lowString}{numbers}{specialChar}"
# allPassword = ["you", "will", "never", "walk", "alone", " ", " ", " ", " "]

# here we ask a user number of password characters want to generate
userPassword = int(input(f"How long password do you want:- "))

'''
here we used choises method from random library to generate a list contains random items
it need two arguments first population which can generate random characters from it 
and the second is the number of characters want to generate 

we use join method to make a genrated list in string type  

'''
genrationPassword = "".join(random.choices(allPassword, k=userPassword))

# code using string module
# genrationPassword = "".join(random.choices(string.printable,k=userPassword))

print(f"Your New Password is '{genrationPassword}'.")
