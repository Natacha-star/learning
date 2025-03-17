# Function to encrypt the message using Kajipotefu cipher
def kajipotefu_encrypt(plaintext):
    # Define the substitution dictionary based on the pattern
    substitution = {
        'k': 'a', 'a': 'k',
        'j': 'i', 'i': 'j',
        'p': 'o', 'o': 'p',
        't': 'e', 'e': 't',
        'f': 'u', 'u': 'f'
    }
    
    encrypted_text = ""
    
    # Iterate through each character of the plaintext
    for char in plaintext:
        # If the character is in the substitution dictionary, replace it
        if char.lower() in substitution:
            # If character is uppercase, preserve the case
            if char.isupper():
                encrypted_text += substitution[char.lower()].upper()
            else:
                encrypted_text += substitution[char]
        else:
            # If the character is not in the dictionary, just add it as is
            encrypted_text += char
    
    return encrypted_text

# Example Usage
plaintext = input("Enter a message to encrypt: ")

# Encrypt the message
encrypted_message = kajipotefu_encrypt(plaintext)
print(f"Encrypted Message: {encrypted_message}")
