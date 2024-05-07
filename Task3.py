import random
import string
length=int(input("Enter the length of the password:"))
print('''Choose character set type for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
characterstring = ""
while(True):
    choice = int(input("Pick a number:"))
    if(choice == 1):
        characterstring += string.ascii_letters
    elif(choice == 2):
        characterstring += string.digits
    elif(choice == 3):
        characterstring += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
 
password = []
for i in range(length):
     randomchar = random.choice(characterstring)
     password.append(randomchar)
print("The random password is " + "".join(password))
