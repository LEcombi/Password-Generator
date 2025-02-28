import random
import string


def generate_password(length=12):
    # Characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))

    return password


if __name__ == "__main__":
    print("Password Generator")
    pass_length = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(pass_length))
