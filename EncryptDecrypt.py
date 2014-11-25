__author__ = 'KH9071'


def decrypt(path,key):
    i = 0
    final = ""
    f = open(path,"rb")
    result =  f.read()
    f.close()


    while i < len(result):
        final += chr((ord(result[i]) - ord(key[i % len(key)]))% 256)
        i += 1
    f = open(path,"wb")
    f.write(final)
    f.close()


def encrypt(path,key):
    result = ""
    f = open(path,"rb")
    data =  f.read()
    f.close()
    i = 0
    while i < len(data):
        result += chr((ord(data[i]) + ord(key[i % len(key)]))% 256)
        i += 1

    f = open(path,"wb")
    f.write(result)
    f.close()

    f.close()
