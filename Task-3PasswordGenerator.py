import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length < 4:
                print("Password should be at least 4 characters long.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def get_password_type():
    print("\nChoose password complexity:")
    print("1. Only Letters (Simple)")
    print("2. Letters and Digits (Medium)")
    print("3. Letters, Digits, and Symbols (Strong)")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Please choose 1, 2, or 3.")


   def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

   
  password = ''.join(random.choice(characters) for _ in range(length))
    return password

def display_password(password):
    print("\n Your Secure Password is:")
    print(f" {password}")

def main():
    print(" Welcome to the Advanced Password Generator 🔒")

    length = get_password_length()
    complexity = get_password_type()
    final_password = generate_password(length, complexity)
    display_password(final_password)

if __name__ == "__main__":
    main()
