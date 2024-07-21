import random
import string
def generate(length,uppercase,lowercase,digits,punctuations):
    ch = ''
    if uppercase:
        ch+=string.ascii_uppercase
    if lowercase:
        ch+=string.ascii_lowercase
    if digits:
        ch+=string.digits
    if punctuations:
        ch+=string.punctuation
    if not ch:
        print("INVALID,NO CHARACTERS FOUND")
        
    password = ''.join(random.choice(ch) for ln in range(length))
    return password
length = int(input("ENTER THE LENGTH OF PASSWORD"))
uppercase = input("NEED UPPERCASE?yes/no:- ").lower() == 'yes'
lowercase = input("NEED LOWERCASE?yes/no:- ").lower() == 'yes'
digits = input("NEED DIGITS?yes/no:- ").lower() == 'yes'
punctuations = input("NEED punctuations?yes/no:- ").lower() == 'yes'
password = generate(length,uppercase,lowercase,digits,punctuations)
print(password)










