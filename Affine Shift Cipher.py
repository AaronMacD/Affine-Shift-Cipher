# -*- coding: utf-8 -*-
"""
Affine Shift Cipher
MTH 225
Aaron MacDougall
Version 12/13/22
"""

key = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 
       'o':14, 'p':15, 'q':16, 'r':17, 't':18, 's':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}

def GCD(a):
    matrices = []
    matrices.append([26, 1, 0])
    matrices.append([a, 0, 1])

    quotient = 0
    remainder = 9999
    
    index = 1
    while remainder > 0:
        quotient = matrices[index-1][0] // matrices [index][0]
        remainder = matrices[index-1][0] % matrices [index][0]
        mSubA = matrices[index-1][1] - quotient * matrices[index][1]
        mSubB = matrices[index-1][2] - quotient * matrices[index][2]
        newList = [remainder, mSubA, mSubB]
        matrices.append(newList)
        index +=1
    
    gcdLocation = len(matrices) - 2
    gcd = matrices[gcdLocation][0]
    if gcd > 1:
        raise ValueError("Invalid A value for the encryption. This value of A is not reversible.")
    else:
        return matrices[gcdLocation][2]

def encrypt(a, b, message):
    messageNumList = []
    encryptedMessage = ""
    for letter in message:
        num = key.get(letter)
        messageNumList.append(num)
    
    
    for searchNum in messageNumList:
        searchNum = (searchNum * a + b) % 26      
        for letter, number in key.items():
            if number == searchNum:
                encryptedMessage += letter
                continue
    
    return encryptedMessage

def decrypt(a, b, encryptedMessage):
    messageNumList = []
    decryptedMessage = ""
    for letter in encryptedMessage:
        num = key.get(letter)
        messageNumList.append(num)
    
    for searchNum in messageNumList:
        searchNum = ((searchNum - b)*a) % 26      
        for letter, number in key.items():
            if number == searchNum:
                decryptedMessage += letter
                continue
    
    return decryptedMessage

def main():
    print("Welcome to the Affine Shift Cipher for the standard 26 letter alphabet. \n")
    validA = False
    inverseMultiplier = 0
    while validA == False:
        a = int(input("Please enter the A value for the Ax + B % 26 formula for the cipher (1-26): "))
    
        try:
            inverseMultiplier = GCD(a)
            validA = True
        except ValueError:
            print("The value for A you entered was invalid due to it not being reversible.")
            validA = False
    
    b = int(input("Please enter the B value for the Ax + B % 26 formula for the cipher: "))
    message = input("Please enter the message you would like encrypted: ")
    
    encryptedMessage = encrypt(a, b, message);
    decryptedMessage = decrypt(inverseMultiplier, b, encryptedMessage)
    
    print("The encrypted message is " + encryptedMessage)
    print("The decrypted message is " + decryptedMessage)
    
if __name__=='__main__':
    main()