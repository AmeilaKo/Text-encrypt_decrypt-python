# encrypt_decrypt-python
This script is for text encryption/decryption.</br>
You will need to provide message to encrypt, key for message encryption and file path to write encrypted message to, the script will create the file if not already existed. </br>
If you would like to read encrypted message from the file, will need to provide the correct key value and the file path.

Usage:
- for encrypt-text-to-file.py script:
  encrypt-text-to-file.py [-h] -message MESSAGE -key KEY -filepath FILEPATH
  encrypt-text-to-file.py: error: the following arguments are required: -message, -key, -filepath

- for decrypt-textfile.py script
  decrypt-textfile.py [-h] -key KEY -filepath FILEPATH
  decrypt-textfile.py: error: the following arguments are required: -key, -filepath

Note: 
  - The file path will be formated as: C:\\users\\username\\Downloads\\file.txt or C:/users/username/Downloads/file.txt
  - This script will overide the content of the chosen file if already existed.
  - Python version 3.11.9

