from cryptography.fernet import Fernet
import cryptography


def encrypt(plain, key):
    text = ""
    for char in plain:
        if (char.isupper()):
            if char.isalpha() == False:
                text +=" "
            else:
                text += chr((ord(char) + key-65) % 26 + 65)
        else:
            if char.isalpha()== False:
                text +=" "
            else:
                text += chr((ord(char) + key - 97) % 26 + 97)
    return text


def decrypt(encoded, key):
    return encrypt(encoded, -key)


def crack(message):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypt_message = fernet.encrypt(message.encode())
    print("original string: ", message)
    print("encrypted string: ", encrypt_message)
    decrypt_message = fernet.decrypt(encrypt_message).decode()
    
    return( decrypt_message )


if __name__ == "__main__":
   
    print(encrypt("zzz",1))
    crack("abc")
