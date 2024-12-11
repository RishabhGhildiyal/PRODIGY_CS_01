def caesar_cipher_encrypt(text, shift):
    """Encrypts text using the Caesar Cipher algorithm."""
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the starting ASCII value (A for uppercase, a for lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap it within the alphabet range (0-25)
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Non-alphabet characters remain unchanged
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    """Decrypts text using the Caesar Cipher algorithm."""
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        print("\n==== Caesar Cipher Program ====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        # Handle invalid menu choices
        try:
            choice = input("Choose an option (1/2/3): ").strip()
            if choice == '3':
                print("Exiting the program. Goodbye!")
                break
            elif choice not in ['1', '2']:
                raise ValueError("Invalid choice! Please select 1, 2, or 3.")
        except ValueError as e:
            print(e)
            continue

        # Get user inputs
        try:
            text = input("Enter your message: ").strip()
            if not text:
                raise ValueError("The message cannot be empty. Please enter a valid message.")
            shift = input("Enter the shift value (e.g., 3): ").strip()
            if not shift.lstrip('-').isdigit():
                raise ValueError("Shift value must be a valid integer. Please try again.")
            shift = int(shift)
        except ValueError as e:
            print(e)
            continue

        # Perform the selected operation
        try:
            if choice == '1':
                encrypted = caesar_cipher_encrypt(text, shift)
                print("\n=== Encryption Result ===")
                print(f"Original Message: {text}")
                print(f"Encrypted Message: {encrypted}")
            elif choice == '2':
                decrypted = caesar_cipher_decrypt(text, shift)
                print("\n=== Decryption Result ===")
                print(f"Encrypted Message: {text}")
                print(f"Decrypted Message: {decrypted}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user. Goodbye!")
