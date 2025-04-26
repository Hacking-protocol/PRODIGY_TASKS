def encrypt_message(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            #Encrypting the message
            shifted_value = (ord(char)-base+shift)%26+base
            result+= chr(shifted_value)        
        else:
            result += char
    return result
print("Starting caesar cipher.....")
message = input("Enter the message you want to encrypt or decrypt....: ")
shift = int(input("Enter the shift value : "))
while True:
        print("Do you want to Encrypt or Decrypt a message?")
        option = input("Enter E for Encryption D for Decryption : " )
        if option == 'E':
            result = encrypt_message(message,shift)
            break
        elif option == 'D':
            result = encrypt_message(message,-shift)
            break
        else:
            print("Enter a valid choixe")
            break
print(f"message : {result} ")
