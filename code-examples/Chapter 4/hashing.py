import hashlib

# Data to hash
data = b'Some important data'

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Update the hash object with the data
hash_object.update(data)

# Get the hexadecimal representation of the hash
hex_dig = hash_object.hexdigest()

print("SHA-256 Hash:", hex_dig)
