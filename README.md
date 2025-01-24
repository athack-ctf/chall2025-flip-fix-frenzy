# Chall - Flip-Fix-Frenzy

> Three binary image files await your analysis: imageA, imageB, and imageC. ImageC was carrying a hidden secret that got corrupted somehow. So, your task is to fix this image and extract the hidden secret with the help of imageA and imageB. Good luck! May the bits be in your favor...

## Type

- [X] **OFF**line
- [ ] **ON**line

## Designer(s)

- Aniket Agarwal

## Description

Using binary image data, this challenge introduces participants to error detection, correction, and steganography. It involves:
- Analyzing a pristine image (imageA) to understand its structure.
- Learning from an encoded, error-free image (imageB) to identify encoding patterns.
- Correcting intentional errors in a corrupted image (imageC) and extracting a hidden message.


**IMPORTANT:** This description will **NOT** be shared with participants.

## Category(ies)

- `stegano`
- `misc`

---

# Project Structure

## 1. HACKME.md

- **[HACKME.md](HACKME.md)**: A teaser or description of the challenge to be shared with participants (in CTFd).

## 2. Source Code

- **[source/README.md](source/README.md)**: Sufficient instructions for building your offline artifacts from source
  code. If your project includes multiple subprojects, please consult us (Anis and Hugo).
- **[source/*](source/)**: Your source code.

## 3. Offline Artifacts

- **[offline-artifacts/*](offline-artifacts/)**: All files (properly named) intended for local download by
  participants (e.g., a binary executable for reverse engineering, a custom-encoded image, etc.). For large files (
  exceeding 100 MB), please consult us (Anis and Hugo).

## 4. Solution

- **[solution/README.md](solution/README.md)**: A detailed writeup of the working solution.
- **[solution/FLAGS.md](solution/FLAGS.md)**: A single markdown file listing all (up-to-date) flags.
- **[solution/*](solution/)**: Any additional files or code necessary for constructing a reproducible solution for the
  challenge (e.g., `PoC.py`, `requirement.txt`, etc.). 
