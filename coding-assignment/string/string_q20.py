'''You have received an encrypted message where each character has been shifted forward by a fixed number in the alphabet. For example, if the shift is 2, 'a' becomes 'c', 'b' becomes 'd', and so on. You need to decrypt the message by shifting the characters back to their original positions.

Problem: Write a Python program that takes an encrypted message and a shift value, then prints the decrypted message.

Example:

Input:
Encrypted message: jgnnq
Shift: 2

Output:
hello  '''

def decrypt_message(encrypted_message, shift):
    decrypted_message = ""
    
    for char in encrypted_message:
        if char.isalpha():  # Check if the character is a letter
            if char.islower():
                new_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            elif char.isupper():
                new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_message += new_char
        else:
            # If the character is not a letter (like a space), just add it as is
            decrypted_message += char
  
    print(decrypted_message)

# Test the function with the provided example
input_encrypted_message = "jgnnq"
shift_value = 2
decrypt_message(input_encrypted_message, shift_value)
