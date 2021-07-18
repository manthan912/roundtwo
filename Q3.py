print ('Welcome')
import random

print("ENTER 1 FOR ENCRYPTION AND 2 FOR DECRYPTION")
n = int(input())
if n == 1:
    print("YOU CHOOSE FOR ENCRYPTION")
    message = input('Enter message you want to encrypt :')
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    key = input("Enter a encrypt key of your Choice (at lease 8 Numbers long): ")
    encrypt = ''
    for i in message:
        position = alphabet.find(i)
        newposition = (position + int(key)) % 94
        encrypt += alphabet[newposition]
    output = (encrypt)
    print('Encrypted Message: ' + (output))
    print('Encryption Key: ' + (key))
else:
    print("YOU CHOOSE FOR DECRYPTION")
    for i in range(1):
        keygen = (random.randint(11111111111, 999999999999999))
    print("")
    message = input('Enter message you want to decrypt:')
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    key = input("Encryption Key:")
    encrypt = ''
    for i in message:
        position = alphabet.find(i)
        newposition = (position + -int(key)) % 94
        encrypt += alphabet[newposition]
    output = (encrypt)
    keyout = (keygen)
    print('Decrypted message: ' + (output))