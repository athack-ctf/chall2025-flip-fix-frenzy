def hamming_decode(encoded_bits):
    """
    Decode 7 bits using Hamming (7,4) decoding, correct single-bit errors, 
    and extract the original 4 data bits.
    """
    # Parity check equations
    s1 = (encoded_bits[0] + encoded_bits[2] + encoded_bits[4] + encoded_bits[6]) % 2
    s2 = (encoded_bits[1] + encoded_bits[2] + encoded_bits[5] + encoded_bits[6]) % 2
    s4 = (encoded_bits[3] + encoded_bits[4] + encoded_bits[5] + encoded_bits[6]) % 2

    # Syndrome value (indicates error position if non-zero)
    error_position = (s4 << 2) | (s2 << 1) | s1

    # Correct the error if there is one
    if error_position != 0:
        error_position -= 1  # Convert to zero-based index
        encoded_bits[error_position] = 1 - encoded_bits[error_position]  # Flip the bit

    # Extract original data bits: d1, d2, d3, d4
    data_bits = [encoded_bits[2], encoded_bits[4], encoded_bits[5], encoded_bits[6]]
    return data_bits

def process_decoded_image(input_file, output_file):
    """
    Process the encoded image file with errors, decode each 7-bit chunk,
    correct single-bit errors, and extract the original binary text.
    """
    decoded_lines = []

    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()  # Remove any extra whitespace or newlines

        # Split the line into 7-bit chunks
        chunks = [line[i:i+7] for i in range(0, len(line), 7)]

        decoded_line = []
        for chunk in chunks:
            # Convert chunk into a list of integers (bits)
            encoded_bits = [int(bit) for bit in chunk]

            # Decode the 7 bits into 4 original data bits
            data_bits = hamming_decode(encoded_bits)

            # Append the data bits to the decoded line
            decoded_line.extend(data_bits)

        # Convert the decoded line back to a string and store it
        decoded_lines.append(''.join(map(str, decoded_line)))

    # Write the decoded lines to the output file
    with open(output_file, 'w') as file:
        for decoded_line in decoded_lines:
            file.write(decoded_line + '\n')

    # Print the decoded lines to the console
    print("Decoded Image:")
    for decoded_line in decoded_lines:
        print(decoded_line)

input_file = 'imageC.txt'  # Input file containing the binary form of image data with errors
output_decoded_file = 'decoded_imageC.txt'  # Output file for the decoded binary image data

# Process the input file and generate the encoded output
process_decoded_image(input_file, output_decoded_file)