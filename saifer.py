import random
import string
import sys
import os
import tkinter as tk
from tkinter import filedialog

#globals
chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

def makeKey(key_name: str) -> str:
    '''Generates a new encryption key

    Args: 
        key_name (str): A name for the new key.

    Returns:
        str: Path it was saved to.
    '''

    # Define the folder path
    folder_path = "Keys"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, key_name+".saiferkey")

    #make a new key based on the chars list and shuffle it
    key = chars.copy()
    random.shuffle(key)

    keyFileptr = open(file_path, "w")
    keystr = ', '.join(key)
    keyFileptr.write(keystr)
    keyFileptr.close()

    return file_path

def encrypt(key_path: str, message_path: str, encrypted_name: str) -> str:
    '''Encrypts a text file with a key

    Args: 
        key_path (str): Path to the saiferkey file used in the encryption.
        message_path (str): Path to the txt file to encrypt.
        encrypted_name (str): A name for the encrypted file.

    Returns:
        str: Path where the saifertxt file can be found.
    '''
        
    keyFileptr = open(f"{key_path}", "r")
    key = keyFileptr.read()
    key = key.split(', ')
    keyFileptr.close()

    messageFileptr = open(f"{message_path}", "r")
    message = messageFileptr.read()
    messageFileptr.close()

    encryptedMessage = ""

    for letter in message:
        #things like â wont be encrypted, weird letters
        if(chars.__contains__(letter)): 
            i = chars.index(letter)
            encryptedMessage += key[i]
        else:
            encryptedMessage += letter

    # Define the folder path
    folder_path = "SaiferTexts"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Define the file path
    file_path = os.path.join(folder_path, encrypted_name+".saifertxt")

    newFileptr = open(file_path, "w")
    newFileptr.write(encryptedMessage)
    newFileptr.close()

    return file_path

def decrypt(key_path: str, encrypted_path: str, decrypted_name: str) -> str:
    '''Encrypts a text file with a key

    Args: 
        key_path (str): Path to the saiferkey file used in the decryption.
        encrypted_path (str): Path to the saifertxt file to decrypt.
        decrypted_name (str): A name for the decrypted file.

    Returns:
        str: The path the decrypted message was saved to.
    '''
    
    keyFileptr = open(f"{key_path}", "r")
    key = keyFileptr.read()
    key = key.split(', ')
    keyFileptr.close()

    messageFileptr = open(f"{encrypted_path}", "r")
    message = messageFileptr.read()
    messageFileptr.close()

    decryptedMessage = ""

    for letter in message:
        #things like â wont be considered, weird letters
        if(key.__contains__(letter)): 
            i = key.index(letter)
            decryptedMessage += chars[i]
        else:
            decryptedMessage += letter

    folder_path = "DeSaiferedTexts"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, decrypted_name+".txt")

    newFileptr = open(file_path, "w")
    newFileptr.write(decryptedMessage)
    newFileptr.close()

    return folder_path
