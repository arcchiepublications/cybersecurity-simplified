from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Generate a key and IV
key = os.urandom(32)  # AES-256 key
iv = os.urandom(16)   # Initialization Vector

# Create a cipher object
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

# Encrypt data
encryptor = cipher.encryptor()
padder = padding.PKCS7(algorithms.AES.block_size).padder()
padded_data = padder.update(b'Confidential data') + padder.finalize()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

print("Ciphertext:", ciphertext)