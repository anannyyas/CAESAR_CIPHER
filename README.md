# CAESAR_CIPHER

This is a simple Python program that implements the Caesar Cipher, one of the oldest and most well-known encryption techniques.

The program allows users to encrypt or decrypt text by entering a shift value between 1 and 25.

## Features

- Encrypt text using the Caesar Cipher
- Decrypt encrypted text
- Supports both uppercase and lowercase letters
- User-friendly command-line interface
- Validates shift values

## How It Works

The Caesar Cipher works by shifting each letter of the alphabet by a fixed number of positions.

Example with a shift of 3:

A → D  
B → E  
C → F  

So:

HELLO → KHOOR

To decrypt a message, the program shifts the letters in the opposite direction. The decryption logic is handled by reversing the shift value before creating the letter mapping. :contentReference[oaicite:0]{index=0}

## Technologies Used

- Python

## How to Run

1. Make sure Python is installed.
2. Open a terminal in the project folder.
3. Run:

```bash
python cipher_caesar.py
```

## Sample Output

```text
Do you want to Encrypt or Decrypt? (E/D): E

Enter the text: Hello World
Enter the shift value (1-25): 3

Encrypted Text: Khoor Zruog
```

```text
Do you want to Encrypt or Decrypt? (E/D): D

Enter the text: Khoor Zruog
Enter the shift value (1-25): 3

Decrypted Text: Hello World
```

## Concepts Practiced

- Functions
- String Manipulation
- User Input Handling
- Conditional Statements
- Basic Cryptography Concepts

## Why I Made This Project

I created this project to practice Python programming and understand how basic encryption techniques work. It helped me learn about string manipulation, character mapping, and function-based program design.

## Author

Ananyaa
