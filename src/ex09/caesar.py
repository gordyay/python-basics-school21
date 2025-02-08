import sys

def caesar():
    if len(sys.argv) == 4:
        exit=0
        mode,text,shift = sys.argv[1:]
        shift = int(shift)
        if mode == "decode":
            shift*=-1
        elif mode != "encode":
            print ("unsupported mode, try \"decode\" or \"encode\"")
            exit=1
        if exit == 0:
            result = caesar_cipher(text, shift)
            if result:
                print(result)
    else:
        print("incorrect number of arguments is given")     
def caesar_cipher(text,shift):
    result = ""
    shift%=26
    for char in text: 
        if char.isascii(): 
            if char.isalpha():
                if char.islower():
                    start=ord("a")
                else:
                    start = ord("A")
                res_char=chr(start+(ord(char)-start+shift)%26)
            else :
                res_char=char
            result+=res_char
        else:
            print("The script does not support your language yet")
            return None
    return result
if __name__ == '__main__':
    caesar()