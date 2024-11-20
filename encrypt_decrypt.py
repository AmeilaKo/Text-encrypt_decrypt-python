# Import all needed modules
import os
from hashlib import sha256
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet

# make a function here called Add_Encrypted_Msg
def Add_Encrypted_Msg(msg_input=str,key_input=str,file_input=str):
    
    # check file path exist, open file for writing
    if os.path.exists(file_input):
        content = open(file_input, 'w')
    else:
        print("File is not found!")
        exit()

    # Convert the key value to 32 url-safe base64-encoded bytes
    # source: from chatgpt & stackoverflow
    key_bytes = sha256(key_input.encode('utf-8')).digest()
    key = Fernet(urlsafe_b64encode(key_bytes))

    # Encrypt the message
    token = key.encrypt(msg_input.encode())

    # Write encrypted message to the file and close file.
    content.write(str(token))
    content.close()
    print("The message has successfully encrypted!")


# make a function here called Read_Encrypted_Msg
def Read_Encrypted_Msg(key_input,file_input):

    # check file path exist, open file for reading
    if os.path.exists(file_input):
        content = open(file_input, 'r')
        content = content.read()
        content = content[2:-1] # get rid of encoded part (b'')
    else:
        print("File is not found!")

    # Convert the key value to 32 url-safe base64-encoded bytes
    # source: from chatgpt & stackoverflow
    key_bytes = sha256(key_input.encode('utf-8')).digest()
    key = Fernet(urlsafe_b64encode(key_bytes))

    # Decrypt the message and display to the terminal
    encrypted_msg = key.decrypt(content).decode()
    print(str(encrypted_msg))

def main():
    print("Warning: This script will overwrite the file of choice!")
    user_choice = input("Would you like to encrypt message to a file (1) or read encrypted message from a file (2): ")
    if user_choice == "1":
        msg_input = input("The message needed to be encrypted: ")
        key_input = input("The key value for message encryption: ")
        file_input = input("File path you would like to write encrypted message to: ")
        
        Add_Encrypted_Msg(msg_input,key_input,file_input)
        exit()
    if user_choice == "2":
        key_input = input("The key you have used to encrypt the msg: ")
        file_input = input("File path you would like to read encrypted message from: ")
        
        Read_Encrypted_Msg(key_input,file_input)
        exit()
    else:
        print("Invalid input, exiting...")

if __name__ == "__main__":
    main()
