def caesar_encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_message += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encrypted_message += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message


def caesar_decrypt(encrypted_message):
    for key in range(26):
        decrypted_message = ""
        for char in encrypted_message:
            if char.isalpha():
                if char.isupper():
                    decrypted_message += chr((ord(char) - 65 - key) % 26 + 65)
                else:
                    decrypted_message += chr((ord(char) - 97 - key) % 26 + 97)
            else:
                decrypted_message += char
        print("Key =", key, "Decrypted message:", decrypted_message)


# Demande à l'utilisateur de saisir une clé de chiffrement
key = int(input("Entrez la clé de chiffrement (un nombre entier) : "))

# Demande à l'utilisateur de saisir le message à chiffrer
message = input("Entrez le message à chiffrer : ")

# Chiffre le message en utilisant le chiffre de César
encrypted_message = caesar_encrypt(message, key)

print("Message chiffré :", encrypted_message)

# Décrypte le message en utilisant une attaque par force brute
caesar_decrypt(encrypted_message)
