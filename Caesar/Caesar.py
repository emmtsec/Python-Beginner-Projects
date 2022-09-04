class Caesar(object):
    def __init__(self):
        print("""
             [1] Encode
             [2] Decode

              """)
    def Caesar_Encode(self):
        Selection = int(input("Please Select: "))
        password = ""
        if Selection == 1:
            Caesar_Encode_Chars = input("Enter Encode Chars: ")
            for Encode in Caesar_Encode_Chars:
                password = password + chr(ord(Encode) + 5)
            print("Before Encode : {}".format(Caesar_Encode_Chars))
            print("After Encode : {}".format(password))
        elif Selection == 2:
            Caesar_Decode_Chars = input("Enter Decode Chars: ")
            for Decode in Caesar_Decode_Chars:
                password = password + chr(ord(Decode) - 5)
            print("Before Encode : {}".format(Caesar_Decode_Chars))
            print("After Decode : {}".format(password))
Caesar_Start = Caesar()
Caesar_Start.Caesar_Encode()