from random import randrange

c="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-="

def askLen():
    try:
        q1=int(input("[>] How long would you like your new password? > "))
        print(f"[*] New password set to be {q1} chars long...\n")
        genPass(q1)
    except (ValueError):
        print("[!] Please use an integer.")
        askLen()

def genPass(newPassLength):
    newPass=""
    for i in range(0,newPassLength):
        xc=randrange(0,len(c))
        newPass=newPass+c[xc]
    print(f"[!] New password: {newPass}\n")

while __name__ == "__main__":
    try:
        askLen()
    except (KeyboardInterrupt):
        print("\n[!] Ctrl+C interrupt... Exiting!")
        quit()