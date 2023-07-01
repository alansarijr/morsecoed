MorseStrings = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':' '}

def encrypt(msg):
    string = msg.upper()
    for ele in range(0, len(string)):
        print(MorseStrings.get(string[ele]), end=" ")
    print("\n")

def decrypt(cypher):
    x = cypher.split()
    for ele in x:
        print(list(MorseStrings.keys())[list(MorseStrings.values()).index(ele)],end="")
    print("\n")

print("Choose Options : \n")
print("1)Encrpt\n2)Decrypt")
opt = input()
if opt == "1":
    encrypt(input("Enter msg to encrypt: \n"))
elif opt == "2":
    decrypt(input("Enter cypher to decrypt: \n"))
else:
    print("enter a valid option")