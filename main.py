import random
import string


def generate_password(length=12):
    # Zeichen, die im Passwort verwendet werden können
    characters = string.ascii_letters + string.digits + string.punctuation

    # Passwort generieren
    password = ''.join(random.choice(characters) for i in range(length))

    return password


if __name__ == "__main__":
    print("Passwort-Generator")
    pass_length = int(input("Gib die gewünschte Länge des Passworts ein: "))
    print("Generiertes Passwort:", generate_password(pass_length))
