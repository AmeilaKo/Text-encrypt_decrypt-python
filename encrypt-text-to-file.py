import os
import argparse
from hashlib import sha256
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet

#Define a functions to collect arguments:


def Add_Encrypted_Msg(Args):
    
    # check file path exist, open file for writing
    if os.path.exists(str(Args.filepath)):
        content = open(str(Args.filepath), 'w')
    else:
        print("No file found. Creating the file...")
        try:
            content = open(str(Args.filepath), 'w')
        except FileNotFoundError:
            print("Can't find the folder that you would like to create the file to!")
            exit()
        except PermissionError:
            print("You don't have permission to create file here!")
            exit()

    # Convert the key value to 32 url-safe base64-encoded bytes
    # source: from chatgpt & stackoverflow
    key_bytes = sha256(f'{Args.key}'.encode('utf-8')).digest()
    key = Fernet(urlsafe_b64encode(key_bytes))

    # Encrypt the message
    token = key.encrypt(f'{Args.message}'.encode())

    # Write encrypted message to the file and close file.
    content.write(str(token))
    content.close()
    print("The message has successfully encrypted!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-message',
    type=str, 
    required= True,
    help="a string to be listed")

    parser.add_argument('-key',
    type=str,
    required= True,
    help="a string to be listed")

    parser.add_argument('-filepath',
    type=str,
    required= True,
    help="a string to be listed")

    Args = parser.parse_args()
    Add_Encrypted_Msg(Args)

if __name__ == '__main__':
    main()
