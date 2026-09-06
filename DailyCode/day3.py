import string
import random

# def password_genrator(len):
#     password_choice = string.ascii_letters + string.digits + string.punctuation
#     password = ""
#     for _ in range(len):
#         password += random.choice(password_choice)
#     return password

class PasswordGenrator:
    def __init__(self,len):
        self.len = len
        self.store_password = []

    def password(self):
        uppercase = random.choice(string.ascii_uppercase)
        lowercase = random.choice(string.ascii_lowercase)
        digit = random.choice(string.digits)
        special = random.choice(string.punctuation)

        password = uppercase + lowercase + digit + special
        # fill out missing char
        characters = (string.ascii_letters + digit + special)

        for _ in range(self.len - 4):
            password += random.choice(characters)

        #shuffle
        shuffle_pass = list(password)
        random.shuffle(shuffle_pass)
        return"".join(shuffle_pass)
        
    def store_pass(self,user_name:str, website:str, notes=None):
        record = {
            "Username"  : user_name,
            "Password":self.password(),
            "Website":website,
            "Notes":notes
        }

        addrecords = self.store_password.append(record)
        return self.store_password
                

password_length = int(input("enter your password length: "))
user_name = input("enter your username for password:")
website_url = input("website url for that you are storing: ")
notes= input("optinal")
password = PasswordGenrator(password_length)
print(password.store_pass(user_name,website_url,notes))