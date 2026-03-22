def encrypt(text, shift=22):
    result = ""
    for char in text:
        if char.isalpha(): 
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  
    return result

def decrypt(text, shift=22):
    return encrypt(text, -shift) 

def main():
    print("Welcome to Caesar Cipher!")
    
    choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice! Please enter E or D.")
        return
    
    text = input("Enter your text: ")
    
    if choice == 'E':
        print("Encrypted text:", encrypt(text))
    else:
        print("Decrypted text:", decrypt(text))

if __name__ == "__main__":
    main()