#!/usr/bin/python
# main code

# from mods.menu import menu, information, exitMessage

# imports
import os 
import sys
import getpass

# import packages
# from ciphers import *

# banner
banner = '''
        _____              __         
       / ___/_____ _____  / /______ __
      / /__/ __/ // / _ \/ __/ -_) \ /
      \___/_/  \_, / .__/\__/\__/_\_\ 
       V:1.0.1/___/_/
Locks only exist to keep honest people honest
'''

# help menu
help_menu = """
      [+] EXAMPLE cryptex -cc -d -t 'This is a string to encrypt' 
      [+] ARG 1. Cipher or Encoding type
            [-cc] --------- Caesar Cipher
            [-vc] --------- Vingenere Cipher
            [-rc] --------- Reverse Cipher
            [-mc] --------- Multiplicative Cipher
            [-dh] --------- Diffie Hellman Key Exchange
            [-xor] -------- XOR Cipher
            [-r13] -------- ROT 13
            [-r47] -------- ROT 47
            [-b64] -------- Base64
            [-bin] -------- Binary
            [-hex] -------- Hex
            [-oct] -------- Octal
            [-133t] ------- L33T 5P34K
            [-mor] -------- Morse Code
            [-pho] -------- Phonetic Alphabet
            [-md5] -------- MD5
            [-sha256] ----- Sha256
            [-gt] --------- Google Translate
      
      [+] ARG 2. Method
            [-e] ---------- Encrypt
            [-d] ---------- Decrypt
            [-b] ---------- Brute Force
            [-w] ---------- Wordlist

      [+] ARG 3. Options
            [-t] ---------- String
            [-i] ---------- Input File
            [-o] ---------- Output File
            [-k] ---------- Encryption Key
            [-r] ---------- Range
"""

# global variables
username = getpass.getuser() # gets username
header = f'[~] {username}@cryptex $ ' # header for user input
remote_path = 'raw.githubusercontent.com/AlexKollar/Cryptex/master' # remote url path
local_path = f'/home/{username}/.Cryptex' if username != 'root' else '/root/.Cryptex' # local path to cryptex
cipher = f'{local_path}/ciphers/' # local path to ciphers

# clears screen
def clear_screen():
    os.system('clear')

# exits cryptex
def exit():
    print('\n[*] Exiting...')
    sys.exit()

# update cryptex
def update():

    print("\n[*] Checking for updates...")

    # get latest version nubmer
    os.system(f"curl https://raw.githubusercontent.com/AlexKollar/Cryptex/master/version.txt | tee ~/.Cryptex/latest.txt")

    # save version nubmers to memory
    current_version = float(open(f"{local_path}/version.txt", "r").read())
    latest_version = float(open(f"{local_path}/latest.txt", "r").read())

    # remove version number file
    os.system("rm -rf ~/.Cryptex/latest.txt")

    # if new version is available, update
    if latest_version > current_version:
        print("\n[+] Update found")
        print("[~] Update Cryptex? [y/n]\n")

        # user input, option
        option = input(f"{header}")
        
        # update
        if option == "y":
            os.system(f"sh ~/.Cryptex/resources/update.sh")

    # otherwise, run main code
    else:
        print("\n[+] Cryptex already up to date")

# command line interface
def cli(arguments):

    # if arguments exist
    if arguments:

        ciphering_option = sys.argv[1]
        remaining_arguments = sys.argv[2:]
        string_args = ' '.join(remaining_arguments)

        try:
            if ciphering_option == '--help' or ciphering_option == '-h':
                print(help_menu)

            elif ciphering_option == '-u' or ciphering_option == '--update':
                update()
            else:
                os.system(f'python3 {cipher}{ciphering_option[1:]}.py {string_args}')
                

        # catches unspecified arguments
        except TypeError:
            print(f'[!!] No Key or Argument was specified\n{help_menu}')

    # crypt console
    else:

        # display banner
        print(banner)
        print('[~] Type "help" for help menu :\n')

        # loop code
        while True:
            # get user input
            user_input = input('\n'+header)

            if user_input == 'help':
                print(help_menu)

            elif user_input == 'exit' or user_input == 'quit':
                exit()
                break

            elif user_input == 'update':
                update()

            elif user_input == 'clear':
                clear_screen()

            else:
                try:
                    ciphering_options = user_input.split(" ")
                    os.system(f'python3 {cipher}{ciphering_options[0].replace("-", "")}.py {" ".join(ciphering_options[1:])}')
                        
                # catches unspecified arguments
                except TypeError:
                    os.system(user_input)

# main code
def main():
    # clear screen
    # clear_screen()

    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    # run command line interface
    cli(arguments_exist)

# run main code
if __name__ == '__main__':
    main()