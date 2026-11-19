import hashlib  

message = "password"
hash = hashlib.sha256(message.encode())
hex_digest = hash.hexdigest()
print(hex_digest)
