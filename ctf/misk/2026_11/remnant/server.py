from base64 import b64encode, b64decode

flag = b64encode(b"Alpaca{?????}")

while True:
    try:
        x = input("Input: ").encode()
        b64decode(bytes(a ^ b for a, b in zip(flag, x))) # remnant
        if x == flag:
            print("Correct!")
        else:
            print("Incorrect...")
    except:
        print("Error...")
