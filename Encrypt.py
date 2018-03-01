from Crypto.Cipher import AES


blocksize = 16
pkcs5Pad = lambda s: s + (blocksize - len(s) % blocksize) * chr(blocksize - len(s) % blocksize) 
pkcs5Unpad = lambda s : s[0:-ord(s[-1])]

class EncryptionLib:

    def __init__(self):
        self.cryptKey = "rianekacahya1234"
        self.ivkey = "rianstaticivkey1"

    def encrypt(self, string):
        string = pkcs5Pad(string)
        cipher = AES.new(self.cryptKey, AES.MODE_CBC, self.ivkey)
        return cipher.encrypt(string).encode("hex")

    def decrypt(self, string):
        string = string.decode("hex")
        cipher = AES.new(self.cryptKey, AES.MODE_CBC, self.ivkey)
        return pkcs5Unpad(cipher.decrypt( string))

if __name__== "__main__":
    a = EncryptionLib()
    encrypt = a.encrypt("rianekacahya")
    decrypt = a.decrypt("f7780052c62730b9295a07a1bb8221cf")
    print "%s" % encrypt
    print "%s" % decrypt