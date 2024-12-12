import os
from cryptography.fernet import Fernet

file_list = []

for file in os.listdir():
    if file == "ransom.py" or file == "generated.key" or file == "ransom_decrypter.py":
        continue
    if os.path.isfile(file): #only files
        file_list.append(file)


with open("generated.key", "rb") as generated_key:
    secret_key = generated_key.read()

for file in file_list:
    with open(file, "rb") as read_file:
        contents = read_file.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as write_file:
        write_file.write(contents_decrypted)
