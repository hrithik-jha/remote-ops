import os

def imgName(loc):
    files = os.listdir(loc)
    return str(len(files) + 1)