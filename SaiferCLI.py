import random
import string
import sys
import os
import tkinter as tk
from tkinter import filedialog
import saifer

sai = saifer

def makeKey_CLI():
    # Define the folder path
    folder_path = "Keys"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Define the file path
    filename = input("Enter a name for your key: ")
    if(filename is None or len(filename.strip()) == 0):
            print("Filename cannot be empty, returning to main menu")
            return
    print("Creating key...")
    path = sai.makeKey(filename)
    print(f"Key created at {path}!")

def encrypt_CLI():
    #GET KEY
    print("Please select a .saiferkey file to be used in encryption...")

    # Create a Tkinter root window
    window = tk.Tk()
    window.withdraw()  # Hide the root window

    # Open a file dialog for selecting a key file
    key_file_path = filedialog.askopenfilename(initialdir=os.getcwd()+"/Keys", title="Select Key",
                                           filetypes=[("Saifer Keys", "*.saiferkey")])

    # Check if a file was selected
    if key_file_path:
        print("Selected file:", key_file_path)
    else:
        print("No file selected. Returning to main menu.")
        return
    
    #GET PLAINTEXT
    print("Please select a .txt file to encrypt...")

    # Open a file dialog for selecting a key file
    txt_file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File",
                                           filetypes=[("Text Files", "*.txt")])

    # Check if a file was selected
    if txt_file_path:
        print("Selected file:", txt_file_path)
    else:
        print("No file selected. Returning to main menu.")
        return
    
    filename = input("Enter a name for the encrypted file: ")
    print("Encrypting...")
    sai.encrypt(key_file_path, txt_file_path, filename)
    print("Encryption Complete!")

def decrypt_CLI():
    #KEYS
    print("Please select a .saiferkey file to be used in decryption...")

    # Create a Tkinter root window
    window = tk.Tk()
    window.withdraw()  # Hide the root window

    # Open a file dialog for selecting a key file
    key_file_path = filedialog.askopenfilename(initialdir=os.getcwd()+"/Keys", title="Select Key",
                                           filetypes=[("Saifer Keys", "*.saiferkey")])

    # Check if a file was selected
    if key_file_path:
        print("Selected file:", key_file_path)
    else:
        print("No file selected. Returning to main menu.")
        return
    
    #SAIFERTEXT
    print("Please select a .saifertxt file to decrypt...")

    # Open a file dialog for selecting a saifertxt file
    saifertxt_file_path = filedialog.askopenfilename(initialdir=os.getcwd()+"/SaiferTexts", title="Select Saifer",
                                           filetypes=[("Saifer Text", "*.saifertxt")])

    # Check if a file was selected
    if saifertxt_file_path:
        print("Selected file:", saifertxt_file_path)
    else:
        print("No file selected. Returning to main menu.")
        return
    
    filename = input("Enter a name for the decrypted file: ")

    print("Decrypting...")
    sai.decrypt(key_file_path, saifertxt_file_path, filename)
    print("Decryption Complete!")

#Main menu functions#
def display_options():
        print("1. Make a Saifer Key")
        print("2. Encrypt a message")
        print("3. Decrypt a message")
        print("4. Exit")

def main():
    print("Saifer main menu: ")
    while True:
        display_options()
        choice = input("Enter your choice: ")

        if choice == '1':
            makeKey_CLI()
        elif choice == '2':
            encrypt_CLI()
        elif choice == '3':
            decrypt_CLI()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()