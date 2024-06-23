from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Encrypt the image by adding the key to each pixel value
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    
    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Decrypt the image by subtracting the key from each pixel value
    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    
    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    while True:
        print("Image Encryption/Decryption Tool")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            image_path = input("Enter the path of the image to encrypt: ")
            output_path = input("Enter the path to save the encrypted image: ")
            key = int(input("Enter the encryption key (an integer): "))
            encrypt_image(image_path, output_path, key)

        elif choice == '2':
            image_path = input("Enter the path of the image to decrypt: ")
            output_path = input("Enter the path to save the decrypted image: ")
            key = int(input("Enter the decryption key (the same integer used for encryption): "))
            decrypt_image(image_path, output_path, key)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
