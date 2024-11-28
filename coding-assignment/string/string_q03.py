'''A spy has sent you a secret message. The message is a string of characters where all the vowels have been replaced with an asterisk (*). You need to write a program that can recover the original message by replacing the asterisks with vowels in a fixed pattern: a, e, i, o, u.

Problem: Write a Python program that replaces all the asterisks in the input string with vowels, in the order a, e, i, o, u, repeatedly.

Example:

Input:
Th* qu*ck br*wn f*x

Output:
Tha quick brown fox'''

def recover_message(message):
    vowels = 'aeiou'
    vowel_index = 0
    message_list = list(message)  
    for i in range(len(message_list)):
        if message_list[i] == '*':
            message_list[i] = vowels[vowel_index]
            vowel_index = (vowel_index + 1) % 5  # Cycle through the vowels
    
    print("".join(message_list))

input_message = "Th* qu*ck br*wn f*x"
recover_message(input_message)
