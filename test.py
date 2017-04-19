import hashlib

if __name__ == '__main__':
    print("hello")
    m = hashlib.md5()
    m.update("hello ".encode())
    m.update("world".encode())
    print(m.digest())
    n = hashlib.md5()
    m.update("hello world".encode())
    print(n.digest())
