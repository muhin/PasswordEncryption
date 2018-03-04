"""
Created on 04 Mar 2018 10:57 PM

@author: muhin
"""


from cryptography.fernet import Fernet


def keyGenerator(plainPassword):
    generatedKey = Fernet.generate_key()
    print("Generated key: " + str(generatedKey, 'utf-8'))
    fernetObj = Fernet(generatedKey)
    plainPasswordBytes = bytes(plainPassword, 'utf-8')
    secretPasswordBytes = fernetObj.encrypt(plainPasswordBytes)
    secretPassword = str(secretPasswordBytes, 'utf-8')
    print("Encrypted password: " + secretPassword)
    #return generatedKey


# print("Please enter your password: ")
plainPassword = input("Please enter your password: ")
keyGenerator(plainPassword)