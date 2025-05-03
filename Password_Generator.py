#My First Python Script

import random
import string

def generate_password(length=12):
	#Get user input for password length
    try:
        length = int(input("Enter the password length: "))
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12  # Default length if input is not a valid number
        
    #Ensure length is positive
    if length <= 0:
        print("Password length must be a positive number. Using default length of 12.")
        length = 12
        
    #Password Generation        
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
	
#Example usage:
print("Generated password:", generate_password())


