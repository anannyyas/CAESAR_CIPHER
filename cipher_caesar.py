def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return "Shift must be an integer value."

    if shift < 1 or shift > 25:   # CConly works with shifts between 1 and 25, becuase total no of alpha are 26
        return "Shift must be an integer between 1 and 25."

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if not encrypt:
        shift = -shift # For decryption, shift in the opposite direction

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    translation_table = str.maketrans(alphabet + alphabet.upper(),shifted_alphabet + shifted_alphabet.upper())
# Create a mapping between original and shifted letters
# Handles both lowercase and uppercase characters
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

# User Input
choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().upper()

text = input("Enter the text: ")
shift = int(input("Enter the shift value (1-25): "))

if choice == "E":
    result = encrypt(text, shift)
    print("\nEncrypted Text:", result)

elif choice == "D":
    result = decrypt(text, shift)
    print("\nDecrypted Text:", result)

else:
    print("Invalid choice. Please enter E for Encrypt or D for Decrypt.")
