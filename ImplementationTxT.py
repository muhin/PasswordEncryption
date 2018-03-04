"""
Created on 04 Mar 2018 11:05 PM

@author: muhin
"""
from cryptography.fernet import Fernet

f = open('credential.txt', 'r')
msg = f.read()
msgSplit = msg.split(',')
# print(msgSplit[2])

bytePassword = bytes(msgSplit[2], 'utf-8')
fernetObj = Fernet("hPh9eN7EXljKDTJ4u4KDURBUQ4IqE42f3IBjwDdzb08=")
decryptedPassword = fernetObj.decrypt(bytePassword)
stringDecryptedPassword = str(decryptedPassword, 'utf-8')
print(stringDecryptedPassword)
