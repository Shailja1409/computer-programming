'''In a cybersecurity class, you are learning about strong passwords. Your teacher has given you a list of passwords and asked you to determine which passwords are "strong". A strong password is defined as one that has at least 8 characters, contains both uppercase and lowercase letters, and has at least one number.

Problem: Write a Python program that reads a list of passwords and prints "strong" if the password is strong, otherwise "weak".

Example:

Input:
Password123 hello123 GoodMorning2021 badpass

Output:
strong weak strong weak'''

def check_password_strength(password):
    if len(password) < 8:
        return "weak"
    
    if not any(c.islower() for c in password) or not any(c.isupper() for c in password):
        return "weak"
    
    if not any(c.isdigit() for c in password):
        return "weak"
    
    return "strong"

def evaluate_passwords(passwords):
    password_list = passwords.split()
    
    for password in password_list:
        print(check_password_strength(password))

input_passwords = "Password123 hello123 GoodMorning2021 badpass"
evaluate_passwords(input_passwords)
