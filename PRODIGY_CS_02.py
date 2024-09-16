from PIL import Image

# Function to encrypt the image
def encrypt_image(image_path, shift_value):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()  # Load the pixel data
    
    # Get image dimensions
    width, height = img.size
    
    # Loop through each pixel and shift RGB values
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]  # Get the RGB values
            # Encrypt by shifting each color value by the shift value
            pixels[x, y] = ((r + shift_value) % 256, (g + shift_value) % 256, (b + shift_value) % 256)
    
    # Save the encrypted image
    encrypted_image_path = "encrypted_image.png"
    img.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")
    return encrypted_image_path

# Function to decrypt the image
def decrypt_image(image_path, shift_value):
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = img.load()  # Load the pixel data
    
    # Get image dimensions
    width, height = img.size
    
    # Loop through each pixel and reverse the shift of RGB values
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]  # Get the encrypted RGB values
            # Decrypt by reversing the shift applied during encryption
            pixels[x, y] = ((r - shift_value) % 256, (g - shift_value) % 256, (b - shift_value) % 256)
    
    # Save the decrypted image
    decrypted_image_path = "decrypted_image.png"
    img.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")
    return decrypted_image_path

# Main function to handle user input and run encryption/decryption
def main():
    print("Image Encryption and Decryption Tool")
    option = input("Would you like to (e)ncrypt or (d)ecrypt an image? ").lower()
    
    # Get image path and shift value from the user
    image_path = input("Enter the image file path: ")
    shift_value = int(input("Enter the shift value (e.g., 1-255): "))
    
    if option == 'e':
        encrypt_image(image_path, shift_value)
    elif option == 'd':
        decrypt_image(image_path, shift_value)
    else:
        print("Invalid option. Please choose either 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
