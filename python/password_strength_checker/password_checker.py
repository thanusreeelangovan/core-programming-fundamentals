import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add at least one digit.")

    # Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.).")

    # Determine strength level
    if strength == 5:
        level = "Very Strong"
    elif strength >= 3:
        level = "Moderate"
    else:
        level = "Weak"

    return level, feedback

def main():
    password = input("Enter a password to check its strength: ")
    level, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {level}")
    if feedback:
        print("Suggestions to improve:")
        for f in feedback:
            print("-", f)

if __name__ == "__main__":
    main()
