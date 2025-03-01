import random
import string

# Function to generate a random password
def generate_password(length=12):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Main block to run the password generator from the command line
if __name__ == "__main__":
    print("Password Generator")
    # Prompt the user to enter the desired password length
    pass_length = int(input("Enter the desired password length: "))
    # Generate and display the password
    print("Generated Password:", generate_password(pass_length))