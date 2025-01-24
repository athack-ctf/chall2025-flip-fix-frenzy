# Building this Challenge

## Step 1:-

Use any 2 images and convert them into their binary equivalent. In this case [dcode](https://www.dcode.fr/binary-image) is used for the same.

## Step 2:-

Save the first image binary as imageA.txt and the second image as imageC.txt. Then use **/source/encoding.py** to feed imageA.txt as input_file. The code will generate two output files with hamming encoded and another with hamming encoding + single-bit errors. Discard the second output file and save the first output file with just hamming encoding as imageB.txt file.

**NOTE**: The explanation of how hamming encoding works is outlined in the comments of the code file.

## Step 3:-

Feed imageC.txt as the input of **/source/hide_flag_in_image.py** which uses the LSB Steganography method to hide the flag in the image binary and then save the updated image binary output in imageC.txt file.

## Step 4:-

Now, use step 2 to feed imageC.txt as input_file and save the output_file_with_errors as imageC.txt. This updated file now contains the hamming encoded image binary with single-bit errors added to it.

## Step 5:-

Give these three image files A, B, and C to the participants and ask them to extract hidden flag from imageC.txt with the help of imageA and B.

