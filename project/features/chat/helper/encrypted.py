from cryptography.fernet import Fernet
class Encrypt:
 def __init__(self):
  

  self.key=Fernet.generate_key()
  self.cipher_suite=Fernet(self.key)

 def encrypted_message(self,message):
   
    return self.cipher_suite.encrypt(message.encode())
 def decrypted_message(self,encrypted_message):
  return self.cipher_suite.decrypt(encrypted_message).decode()