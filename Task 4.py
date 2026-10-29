"""INFOZATECH Task 4: Password Generator
Run with: python task4_password_generator.py
Uses Python's secrets module for security-oriented randomness.
"""
import secrets
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    groups = []
    if use_upper:
        groups.append(string.ascii_uppercase)
    if use_lower:
        groups.append(string.ascii_lowercase)
    if use_digits:
        groups.append(string.digits)
    if use_symbols:
        groups.append("!@#$%^&*()-_=+[]{};:,.?/")

    if not groups:
        raise ValueError("Select at least one character type.")
    if length < len(groups):
        raise ValueError(f"Length must be at least {len(groups)} for the selected character types.")

    # Include at least one character from every selected group.
    password_chars = [secrets.choice(group) for group in groups]
    all_chars = "".join(groups)
    password_chars.extend(secrets.choice(all_chars) for _ in range(length - len(password_chars)))

    # Securely shuffle characters so required characters aren't fixed at the start.
    for index in range(len(password_chars) - 1, 0, -1):
        swap_index = secrets.randbelow(index + 1)
        password_chars[index], password_chars[swap_index] = password_chars[swap_index], password_chars[index]
    return "".join(password_chars)


def ask_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter y or n.")


def main():
    print("===== PASSWORD GENERATOR =====")
    try:
        length = int(input("Desired password length (4-128): ").strip())
    except ValueError:
        print("Length must be a whole number.")
        return

    if not 4 <= length <= 128:
        print("Please choose a length between 4 and 128.")
        return

    use_upper = ask_yes_no("Include uppercase letters?")
    use_lower = ask_yes_no("Include lowercase letters?")
    use_digits = ask_yes_no("Include digits?")
    use_symbols = ask_yes_no("Include symbols?")

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print("\nGenerated password:")
    print(password)
    print("For safety, do not share this password or store it in an unprotected file.")


if __name__ == "__main__":
    main()
