# A simple program to add to and view password log on an encrypted .txt file
# Chris, 30/01/2023
from cryptography.fernet import Fernet


''' this fxn creates unique key to access unencrypted passwords file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    file = open("key.key", "rb")
    key_ = file.read()
    file.close()
    return key_


master_pswd = "casey"
master = input("What is the master password? ")
key = load_key() + master_pswd.encode()
fer = Fernet(key)  # initialises encryption module


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    user = input("Enter account name: ")
    pswd = input("Enter password: ")

    with open('passwords.txt', 'a') as f:  # with opens and closes file, a adds to end, opens new otherwise
        f.write(user + "|" + fer.encrypt(pswd.encode()).decode() + "\n")


while True and master == master_pswd:
    mode = input("Would you like to add a password, or view existing ones?(view, add, q to quit) ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
