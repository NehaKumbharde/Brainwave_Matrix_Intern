import string
import re

# List of common weak passwords for uniqueness check
COMMON_PASSWORDS = ["123456", "password", "123456789", "qwerty", "abc123"]

def check_length(password):
    # Minimum password length of 12 characters
    if len(password) >= 10:
        return True
    return False

def check_complexity(password):
    # Check if the password contains at least one lowercase letter, uppercase letter, digit, and special character
    has_lower = re.search(r'[a-z]', password) is not None
    has_upper = re.search(r'[A-Z]', password) is not None
    has_digit = re.search(r'[0-9]', password) is not None
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    return has_lower and has_upper and has_digit and has_special

def check_uniqueness(password):
    # Check against a list of common passwords
    if password.lower() in COMMON_PASSWORDS:
        return False
    return True

def evaluate_password(password):
    feedback = []

    # Check length
    if not check_length(password):
        feedback.append("Password is too short. Aim for at least 10 characters.")

    # Check complexity
    if not check_complexity(password):
        feedback.append("Password lacks complexity. Use a mix of lowercase, uppercase, digits, and special characters.")

    # Check uniqueness
    if not check_uniqueness(password):
        feedback.append("Password is too common. Try using a more unique password.")

    # Strength rating based on length and complexity
    strength_score = 0
    if check_length(password):
        strength_score += 1
    if check_complexity(password):
        strength_score += 1
    if check_uniqueness(password):
        strength_score += 1

    if strength_score == 3:
        feedback.append("Password is strong!")
    elif strength_score == 2:
        feedback.append("Password is moderate. Consider improving it.")
    else:
        feedback.append("Password is weak. Try making it longer and more complex.")

    return feedback

# Example usage
password = "Neha@06kumbharde"
feedback = evaluate_password(password)
for line in feedback:
    print(line)

