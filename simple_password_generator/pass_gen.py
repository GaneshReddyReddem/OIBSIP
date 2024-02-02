import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type (letters, numbers, or symbols) must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Error: Password length must be a positive integer.")
            return

        use_letters = input("Include letters (uppercase and lowercase)? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password:
            print(f"\nGenerated Password: {password}")
    
    except ValueError:
        print("Error: Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
