"""
Created on 04 Mar 2018 11:02 PM

@author: muhin
"""

import openpyxl
from cryptography.fernet import Fernet
#cipher_key = Fernet.generate_key()
#print(cipher_key)
#print("hello")

readWb = openpyxl.load_workbook("E:\\pTest\\readData.xlsx")
readSheet = readWb.get_sheet_by_name("credential")
col_1 = readSheet['A2'].value
col_2 = readSheet['B2'].value
col_3 = readSheet['C2'].value
col_4 = readSheet['D2'].value
bCol_3 = bytes(col_3, 'utf-8')
print(bCol_3)

#generatedKey = Fernet.generate_key()
#print("key: " + str(generatedKey))
fernetObj = Fernet("X1rC3HgC6BaLJR30s6fQEmF-LKDljRhkT1i6d0ZyEeY=")
#secretPass = fernetObj.encrypt(b"admin")
#print(secretPass)
openPass = fernetObj.decrypt(bCol_3)
print(openPass)
sOpenPass = str(openPass, 'utf-8')
print(sOpenPass)
