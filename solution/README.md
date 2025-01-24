# How to Solve the Challenge?

## Step 1:-

Identify the hamming (7,4) encoding pattern by looking at imageA and imageB files. imageA is a perfectly normal binary with no encoding or errors. imageB on the other hand seems to be manipulated by adding encoded parity bits for error correction. It's often used in the transmission of signals or important data to avoid the risk of data corruption for up to a single-bit error. 

parity bits position are - p1, p2, d1, p4, d2, d3, d4 (total 7 bits of which 4 data and 3 parity bits). 

## Step 2:-

Once the pattern is identified in imageC.txt, write the decoding algorithm like the one uploaded in **/solution/decoding.py**. This code is explained with the help of comments. 

## Step 3:- 

Now, feed imageC.txt in the code developed for decoding and correcting the single-bit error induced in the image binary. The decoded binary should look the same as the one uploaded in **/solution/decoded_imageC.txt** 

## Step 4:-

Lastly, feed the decoded_imageC.txt to **/solution/extract_flag_from_image.py** and obtain the hidden flag wohooo!!. 

Congratulations on solving this challenge based on hamming encoding and single-bit error correction. I hope you liked the challenge!



