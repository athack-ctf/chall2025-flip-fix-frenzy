import random

def calculate_parity_bits(data_bits):
    """
    Calculate the three parity bits for the 4 data bits.
    
    Parity bit positions:
    p1 -> Covers bits 1, 3, 5, 7
    p2 -> Covers bits 2, 3, 6, 7
    p4 -> Covers bits 4, 5, 6, 7
    """
    p1 = (data_bits[0] + data_bits[1] + data_bits[3]) % 2
    p2 = (data_bits[0] + data_bits[2] + data_bits[3]) % 2
    p4 = (data_bits[1] + data_bits[2] + data_bits[3]) % 2

    return [p1, p2, p4]

def hamming_encode(data_bits):
    """
    Encode 4 data bits into 7 bits using Hamming (7,4) encoding.
    """
    parity_bits = calculate_parity_bits(data_bits)

    # Arrange bits in the order: p1, p2, d1, p4, d2, d3, d4
    encoded_bits = [
        parity_bits[0],  # p1
        parity_bits[1],  # p2
        data_bits[0],    # d1
        parity_bits[2],  # p4
        data_bits[1],    # d2
        data_bits[2],    # d3
        data_bits[3]     # d4
    ]
    return encoded_bits

def introduce_single_bit_error(encoded_bits):
    """
    Introduce a single bit error in the encoded 7 bits.
    """
    error_position = random.randint(0, 6)  # Randomly select a bit position to flip
    encoded_bits[error_position] = 1 - encoded_bits[error_position]  # Flip the bit
    return encoded_bits

def process_image_file(input_file, output_file):
    """
    Process the input image binary file, encode each line using Hamming (7,4),
    and write the encoded output to a new file and print it to the console.
    """
    encoded_lines = []

    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()  # Remove any extra whitespace or newlines

        # Split the line into 4-bit chunks
        chunks = [line[i:i+4] for i in range(0, len(line), 4)]

        encoded_line = []
        for chunk in chunks:
            # Convert chunk into a list of integers (bits)
            data_bits = [int(bit) for bit in chunk]

            # Pad with zeros if the chunk is less than 4 bits
            while len(data_bits) < 4:
                data_bits.append(0)

            # Encode the 4 data bits into 7 bits
            encoded_bits = hamming_encode(data_bits)

            # Append the encoded bits to the encoded line
            encoded_line.extend(encoded_bits)

        # Convert the encoded line back to a string and store it
        encoded_lines.append(''.join(map(str, encoded_line)))

    # Write the encoded lines to the output file
    with open(output_file, 'w') as file:
        for encoded_line in encoded_lines:
            file.write(encoded_line + '\n')

    # Print the encoded lines to the console
    print("Encoded Image:")
    for encoded_line in encoded_lines:
        print(encoded_line)

def process_image_with_errors(input_file, output_file):
    """
    Process the input image binary file, encode each line using Hamming (7,4),
    introduce a single bit error in every 7-bit encoding, and write the output to a new file.
    """
    encoded_lines_with_errors = []

    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()  # Remove any extra whitespace or newlines

        # Split the line into 4-bit chunks
        chunks = [line[i:i+4] for i in range(0, len(line), 4)]

        encoded_line = []
        for chunk in chunks:
            # Convert chunk into a list of integers (bits)
            data_bits = [int(bit) for bit in chunk]

            # Pad with zeros if the chunk is less than 4 bits
            while len(data_bits) < 4:
                data_bits.append(0)

            # Encode the 4 data bits into 7 bits
            encoded_bits = hamming_encode(data_bits)

            # Introduce a single bit error
            encoded_bits_with_error = introduce_single_bit_error(encoded_bits)

            # Append the encoded bits with error to the encoded line
            encoded_line.extend(encoded_bits_with_error)

        # Convert the encoded line back to a string and store it
        encoded_lines_with_errors.append(''.join(map(str, encoded_line)))

    # Write the encoded lines with errors to the output file
    with open(output_file, 'w') as file:
        for encoded_line in encoded_lines_with_errors:
            file.write(encoded_line + '\n')

    # Print the encoded lines with errors to the console
    print("Encoded Image with Errors:")
    for encoded_line in encoded_lines_with_errors:
        print(encoded_line)

# Specify the input and output file paths
input_file = 'imageC.txt'  # Input file containing the binary data
output_file = 'imageBb.txt'  # Output file for the encoded data
output_file_with_errors = 'imageCc.txt'  # Output file for the encoded data with errors

# Process the input file and generate the encoded output
process_image_file(input_file, output_file)
process_image_with_errors(input_file, output_file_with_errors)
