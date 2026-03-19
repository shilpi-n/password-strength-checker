import re

import re

def check_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number")

    # Special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$ etc.)")

    # Strength decision
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback

password = input("Enter your password: ")

strength, feedback = check_password(password)

print("Password Strength:", strength)

if feedback:
    print("Suggestions to improve:")
    for item in feedback:
        print("-", item)