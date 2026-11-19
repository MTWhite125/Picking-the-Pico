import hashlib
userFile = "users.txt"
        
def hashPassword(password):
    hash = hashlib.sha256(password.encode())
    hex_digest = hash.hexdigest()
    return hex_digest

def createAccount(username, password):
    with open(userFile, "a") as f:
        f.write(f"{username},{password}\n")
    return True

def login(username, password):
    grantAccess = False;
    with open(userFile, "r") as f:
        for i in f.readlines():
            entry = f"{username},{password}\n"
            if (i == entry):
                grantAccess = True
                break
    return grantAccess
