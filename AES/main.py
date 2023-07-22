import binascii
import os
from AES import AESAlgo

class AESMain():
    def main():
        # input the msg from user which will be encrypt
        print("+==============================The MSG to be encrypt======================================+")
        userInputMsg = input("Please enter the message here:\n>>> ")
        # generate a random secret key with the library "os" with the length 256-bit
        # then set it as a setKey()
        secretKey = os.urandom(32)
        aes = AESAlgo(secretKey, userInputMsg)
        #aes.setKey(secretKey)
        print("\n+==============================The secret key======================================+")
        print(binascii.hexlify(secretKey))

        # encrypt the msg with the random secret key "secretKey" 
        # using the funtion "encrypt_AES_GCM" from file "AES.py"
        encryptedMsg = aes.encrypt_AES_GCM(aes.getMsg().encode("utf8"), aes.getKey())

        # dencrypt the msg with the same random secret key "secretKey" 
        # using the funtion from file "AES.py"
        decryptedMsg = aes.decrypt_AES_GCM(encryptedMsg, aes.getKey()).decode("utf8")

        # print the msg after dencrypting and decoding in "utf-8"
        print("\n+==============================The MSG after dencrypt======================================+")
        print(">>>",decryptedMsg)


if __name__ == "__main__":
    AESMain.main()