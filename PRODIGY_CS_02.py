from PIL import Image
import numpy as np

def encrypt_img(img_path,out_path,key):
    image = Image.open(img_path).convert('RGB') # creating object fro the image to work on that image 
    img_arr = np.array(image,dtype=np.uint8)    # converting image into an array,contains each pixel value range from 0-255 explicit saying it should be in 8bit unsigned int
    key_uint8 = np.uint8(key)
    encrypt_arr = img_arr ^ key_uint8 #performs xor operation to each pixel value in image array
    #convert this encrypted image array into image
    encrypted_img = Image.fromarray(encrypt_arr)#unsigned 8bit integer is standard representation for image pixels
    #saving the encrypted image in a location
    encrypted_img.save(out_path)

def decrypt_img(img_path,out_path,key):
    encrypt_img(img_path,out_path,key)

img_path = input("Enter path of the image you want to Encrypt or Decrypt : ")
out_path = input("Where you want to save the image : ")
key = input("ENter the key must be in range 0-255 : ")
option = int(input("Enter your choice \n 1)Encryption 2)Decryption "))
if option == 1:
    encrypt_img(img_path,out_path,key)
    print(f"Encrypted image saved at {out_path}")
elif option == 2:
    decrypt_img(img_path,out_path,key)
    print(f"Decrypted image saved at {out_path}")
else:
    print("Enter a valid choice") 

#############################################################################################################
# you must specify the image extension along with the path Ex: D:\folder\imgname.extension for the img_path #
# And Ex: D:\folder\imagename.extension for saving the encrypted image [out_path]                           #
#############################################################################################################