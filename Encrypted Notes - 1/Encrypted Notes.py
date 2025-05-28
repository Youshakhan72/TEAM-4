from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_note(note):
    return cipher.encrypt(note.encode())

def decrypt_note(encrypted):
    return cipher.decrypt(encrypted).decode()

note = input("Write a secret note: ")
enc = encrypt_note(note)
print("Encrypted:", enc)

show = input("Decrypt? (y/n): ")
if show.lower() == 'y':
    print("Decrypted:", decrypt_note(enc))