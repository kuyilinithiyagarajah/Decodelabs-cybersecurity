# Project 2: Basic Encryption & Decryption
# Caesar Cipher | DecodeLabs Batch 2026

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, 26 - shift)

def main():
    print("=" * 40)
    print("   Caesar Cipher - Encryption Tool")
    print("=" * 40)

    text = input("\nEnter your message: ")
    shift = int(input("Enter shift key (1-25): "))

    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print("\n--- Output ---")
    print(f"Original  : {text}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")
    print("-" * 40)

if __name__ == "__main__":
    main()
