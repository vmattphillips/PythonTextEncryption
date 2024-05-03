import random
import string
import sys
import os
import saifer
import argparse

# UNFINISHED

sai = saifer

def help(option):
    if option is None:
        print("-h, --help\t Show this help dialog or use with anther argument for further explanations. Ex: -hm, -hk")
        print("-m, --mode\t The mode in which you want the program to run in.")
        print("-k, --key\t The path of the key used in encryption or decryption.")
        print("-t, --text\t The path of the text file to be encrypted.")
        print("-s, --saifertext\t The path of the saifertext file to be decrypted.")
        print("")

def main():
    desc = "**************************"
    desc += " SAIFER Encryption "
    desc += "**************************"
    parser = argparse.ArgumentParser(description=desc, add_help=False)
    parser.add_argument("-h", "--help", action=argparse.BooleanOptionalAction)
    #parser.add_argument("-h", "--help", type=str)
    parser.add_argument("-m", "--mode", type=int)
    parser.add_argument("-k", "--key", type=str)
    parser.add_argument("-t", "--text", type=str)
    parser.add_argument("-s", "--saifertext")

    args = parser.parse_args()

    if args.help:
        help(None)

    # TODO Connect these to the saifer.py backend 
    if(args.mode == 0):
        print("Make Key")
    elif(args.mode == 1):
        print("Encrypt")
    elif(args.mode == 2):
        print("Decrypt")
    else:
        print("error")



main()