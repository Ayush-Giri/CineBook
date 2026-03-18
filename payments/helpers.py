import secrets
import string

def generate_txn_id():
    prefix = "CINE"
    random_part = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return prefix + random_part
