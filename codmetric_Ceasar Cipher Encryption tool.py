def encrypt(text: str, shift: int) -> str:
    """
    Encrypts the given text using Caesar cipher with the specified shift value.
    
    Args:
        text: The plaintext to encrypt
        shift: The number of positions to shift each character
        
    Returns:
        The encrypted ciphertext
    """
    encrypted_text = []
    for char in text:
        if char.isupper():
            encrypted_text.append(chr((ord(char) + shift - 65) % 26 + 65))
        elif char.islower():
            encrypted_text.append(chr((ord(char) + shift - 97) % 26 + 97))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt(text: str, shift: int) -> str:
    """
    Decrypts the given ciphertext using Caesar cipher with the specified shift value.
    
    Args:
        text: The ciphertext to decrypt
        shift: The number of positions the characters were originally shifted
        
    Returns:
        The decrypted plaintext
    """
    return encrypt(text, -shift)

def main():
    """Main function to run the Caesar cipher tool."""
    print("Caesar Cipher Encryption Tool")
    print("----------------------------")
    
    # Get user input
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (integer): "))
    
    # Encrypt the text
    encrypted = encrypt(text, shift)
    print(f"\nEncrypted text: {encrypted}")
    
    # Decrypt the text
    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted text: {decrypted}")

if __name__ == "__main__":
    main()