print("!" * 60)
print("!!!!!!!      This is a Caesar Cipher Program       !!!!!!!!!!!")
print("!" * 60)


message = input("Enter the text : ")

message = message.upper()

key = (int(input("Enter the key : ")))

print("Decide if you want to encrypt or decrypt")

mode = input("1. Encrypt \n2. Decrypt \n>")

# every possible symbol that can be encrypted
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
#LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''



for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        elif mode == '1':
            num = num + key
        elif mode == '2':
            num = num - key
        if mode == 'ENCRYPT':
            num = num + key
        elif mode == 'DECRYPT':
            num = num - key



        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)


        translated = translated + LETTERS[num]

    else:

        translated = translated + symbol

print(translated)

