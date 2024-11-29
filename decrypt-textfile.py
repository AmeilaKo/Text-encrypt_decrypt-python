import os
import argparse
from hashlib import sha256
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet

def Read_Encrypted_Msg(Args):

    # check file path exist, open file for reading
    if os.path.exists(str(Args.filepath)):
        content = open(str(Args.filepath), 'r')
        content = content.read()
        content = content[2:-1] # get rid of encoded part (b'')
    else:
        print("File is not found!")

    # Convert the key value to 32 url-safe base64-encoded bytes
    # source: from chatgpt & stackoverflow
    key_bytes = sha256(str(Args.key).encode('utf-8')).digest()
    key = Fernet(urlsafe_b64encode(key_bytes))

    # Decrypt the message and display to the terminal
    encrypted_msg = key.decrypt(content).decode()
    print("The message is: " + str(encrypted_msg))

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-key',
    type=str,
    required= True,
    help="a string to be listed")

    parser.add_argument('-filepath',
    type=str,
    required= True,
    help="a string to be listed")

    Args = parser.parse_args()
    Read_Encrypted_Msg(Args)

if __name__ == '__main__':
    main()
