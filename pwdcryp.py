from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b"dxdeznftmpmunayq")
with open('C:\\Users\\fabs\\Documents\\Code\\Python\\Network\\gapppython2.bin', 'wb') as file_object: file_object.write(ciphered_text)
