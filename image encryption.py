from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path):
    # Open the image
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Encrypt the image by swapping pixel values and adding a constant
    encrypted_array = np.copy(img_array)
    height, width, channels = img_array.shape

    # Simple encryption: swap pixels and add a constant
    for i in range(height):
        for j in range(width):
            # Swap pixel values with the next pixel
            if j < width - 1:
                encrypted_array[i, j], encrypted_array[i, j + 1] = img_array[i, j + 1], img_array[i, j]
            # Add a constant value to each pixel
            encrypted_array[i, j] = (encrypted_array[i, j] + 50) % 256

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path):
    # Open the encrypted image
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Decrypt the image by reversing the operations
    decrypted_array = np.copy(img_array)
    height, width, channels = img_array.shape

    # Simple decryption: subtract the constant and swap pixels back
    for i in range(height):
        for j in range(width):
            # Subtract the constant value from each pixel
            decrypted_array[i, j] = (decrypted_array[i, j] - 50) % 256
            # Swap pixel values back
            if j > 0:
                decrypted_array[i, j], decrypted_array[i, j - 1] = img_array[i, j - 1], img_array[i, j]

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

# Example usage
if __name__ == "__main__":
    encrypt_image('input_image.png', 'encrypted_image.png')
    decrypt_image('encrypted_image.png', 'decrypted_image.png')
