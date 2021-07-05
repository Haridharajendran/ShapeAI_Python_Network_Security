import hashlib
message = "Happy birthday".encode()
print("MD5:", hashlib.md5(message).hexdigest())
print("SHA-256:", hashlib.sha256(message).hexdigest())
print("SHA-512:", hashlib.sha512(message).hexdigest())
print("SHA-3-256:", hashlib.sha3_256(message).hexdigest())
print("SHA-3-512:", hashlib.sha3_512(message).hexdigest())
print("BLAKE2c:", hashlib.blake2s(message).hexdigest())
print("BLAKE2b:", hashlib.blake2b(message).hexdigest())
