import base64
import sys

def encode_to_base64(text: str) -> str:
    """
    Encodes a string to Base64 format.
    
    Args:
        text: The string to encode
        
    Returns:
        Base64 encoded string
    """
    if not text:
        return "Error: Input text is empty"
    
    try:
        # Convert string to bytes, then encode to Base64 bytes, then decode to string
        encoded_bytes = base64.b64encode(text.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Encoding error: {str(e)}"

def decode_from_base64(encoded_text: str) -> str:
    """
    Decodes a Base64 string back to its original form.
    
    Args:
        encoded_text: The Base64 encoded string
        
    Returns:
        Decoded original string
    """
    if not encoded_text:
        return "Error: Input text is empty"
    
    try:
        # Convert Base64 string to bytes, decode to original bytes, then to string
        decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Decoding error: {str(e)}"

def display_menu() -> None:
    """Displays the program menu options."""
    print("\nBase64 Encoder/Decoder Tool")
    print("--------------------------")
    print("1. Encode text to Base64")
    print("2. Decode Base64 to text")
    print("3. Exit")

def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            text = input("Enter text to encode: ")
            if not text.strip():
                print("Error: Input cannot be empty")
                continue
            encoded = encode_to_base64(text)
            print(f"\nEncoded result: {encoded}")
            
        elif choice == '2':
            text = input("Enter Base64 to decode: ")
            if not text.strip():
                print("Error: Input cannot be empty")
                continue
            decoded = decode_from_base64(text)
            print(f"\nDecoded result: {decoded}")
            
        elif choice == '3':
            print("Exiting program...")
            sys.exit(0)
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()