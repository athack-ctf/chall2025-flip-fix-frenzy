def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def embed_text_in_binary_image(image_binary, text):
    """Embeds the given text into the binary image using LSB steganography."""
    # Convert text to binary
    binary_text = text_to_binary(text) + '00000000'  # Append NULL terminator

    # Flattened the image binary into a single string for easier manipulation
    image_binary_flat = ''.join(image_binary.split())

    if len(binary_text) > len(image_binary_flat):
        raise ValueError("Text is too long to embed in the given binary image.")

    # Embeded the binary text into the least significant bits of the image binary
    embedded_binary = list(image_binary_flat)
    for i, bit in enumerate(binary_text):
        embedded_binary[i] = embedded_binary[i][:-1] + bit

    # Reconstructed the binary image with the embedded text
    embedded_image_binary = ''.join(embedded_binary)

    # Formated the embedded binary back into the original image shape
    formatted_embedded_image = '\n'.join(
        [embedded_image_binary[i:i+len(image_binary.split('\n')[0])]
         for i in range(0, len(embedded_image_binary), len(image_binary.split('\n')[0]))]
    )

    return formatted_embedded_image

# Original binary image
image_binary = """1111111111111111111111111111111111111111
1111111111111111111100001111111111111111
1111111111111111111000000011111111111111
1111111111111110000000000000111111111111
1111111111111110100000000000011111111111
1111111111111111110000000000001111111111
1111111111011111110000000000000111111111
1111111111101111111000000000000111111111
1111111111101111111000000000000011111111
1111111111011111110000000000000011111111
1111111111011111111100000000000011111111
1111111111111111111100000000000011111111
1111111111110000001100000000000111111111
1111111110110000001100000000000011111111
1111111100111111111100000000000011111111
1111111111111011111111000000000001111111
1111111111001111111111100000000000111111
1111111111111101111001100000000011111111
1111111111111001110000100000000011111111
1111111111111111110000110000000011111111
1111111111011111111000111000000011111111
1111111111111111111001011100000011111111
1111111111111111111001111111111111111111
1111111111111111111000111111111111111111
1111111111111111111010111111111111111111
1111111111111111110110111111111111111111
1111111111111111111111011111111111111111
1111111111111111101111011111111111111111
1111111111111111111111001111111111111111
1111111111111111100011011111111111111111
1111111111111100000000000011111111111111
1111111111111100000000000011111111111111
1111111111111000000000000001111111111111
1111111111110000000000000000111111111111
1111111111111111100000011111111111111111
"""

# Text to hide
flag = "ATHACK{!!!J3st3r_wAs_vvR0ng!!!}"

# Embed the flag into the binary image
embedded_image = embed_text_in_binary_image(image_binary, flag)

# Output the embedded binary image
print("Embedded Binary Image:")
print(embedded_image)