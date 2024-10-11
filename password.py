import re
"""
█████▄░▄████▄░▄██████░▄██████░██░██░██░▄█████▄░█████▄░██████▄
██░░██░██░░██░██░░░░░░██░░░░░░██░██░██░██░░░██░██░░██░██░░░██
█████▀░██░░██░▀█████▄░▀█████▄░██░██░██░██░░░██░█████▀░██░░░██
██░░░░░██████░░░░░░██░░░░░░██░██░██░██░██░░░██░██░░██░██░░░██
██░░░░░██░░██░██████▀░██████▀░▀██▀▀██▀░▀█████▀░██░░██░██████▀
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""

def check_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_character_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_character_criteria])

    strength = "Weak"
    if criteria_met >= 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"

    feedback = [
        "Length of at least 8 characters" if not length_criteria else "",
        "At least one lowercase letter" if not lowercase_criteria else "",
        "At least one uppercase letter" if not uppercase_criteria else "",
        "At least one number" if not number_criteria else "",
        "At least one special character" if not special_character_criteria else ""
    ]

    feedback = [f for f in feedback if f]

    return strength, feedback

def main():
    password = input("Enter a password to check its strength: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("To improve your password, consider the following:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    main()
