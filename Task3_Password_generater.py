import random
import string

characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

length = int(input("Enter the password length: "))

password = ''.join(random.choices(characters, k=length))

print("Password:", password)