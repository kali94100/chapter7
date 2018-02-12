import os

def run(**ars):
    print "[*] In direlister module."
    files = os.listdir(".")

    return str(files)
