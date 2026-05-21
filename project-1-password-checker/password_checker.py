# Password Strength Checker
# Project 1 - DecodeLabs Cybersecurity Internship
# Checks if a password is Weak, Medium, or Strong

def check_password_strength(password):
    
    # Rule 1: Password must be at least 8 characters
    if len(password) < 8:
        return "WEAK - Too short (minimum 8 characters)"

    # Rule 2: Check for uppercase letters (A-Z)
    has_upper = any(char.isupper() for char in password)
    
    # Rule 3: Check for numbers (0-9)
    has_digit = any(char.isdigit() for char in password)
    
    # Rule 4: Check for special symbols
    has_symbol = any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for char in password)

    # Count how many rules are passed
    score = sum([has_upper, has_digit, has_symbol])

    # Rate the password based on score
    if score == 3:
        return "STRONG - Great password!"
    elif score == 2:
        return "MEDIUM - Consider adding more variety"
    else:
        return "WEAK - Add uppercase letters, numbers, and symbols"


# Main Program - Get input from user and show result
password = input("Enter a password to check: ")
result = check_password_strength(password)
print("Password Strength:", result)
