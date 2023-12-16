import hashlib

from cryptography.fernet import Fernet

#user password
def user_password( user_password: str) -> str:
    combined_string = f"{user_password}"
    user_password = hashlib.sha256(combined_string.encode()).hexdigest()
    return user_password




def encrypt_password(password: str) -> str:
    #bill's password
    #generes a key
    clave = Fernet.generate_key()
    # Create the cipher suite
    cipher_suite = Fernet(clave)
    
    encrypted_password = cipher_suite.encrypt(password.encode())
    return {"encrypted_password": encrypted_password, "clave": clave}

def decrypt_password(encrypted_password: bytes, clave:bytes) -> str:
   # Create the cipher suite
   cipher_suite = Fernet(clave)
   decrypted_password = cipher_suite.decrypt(encrypted_password)
   return decrypted_password

