import hashlib
from dbhandler import dbhandler

def encrypt_password(password):
    sha_signature = \
        hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

