import random
import string

secret_message = "Somewhere over the rainbow 123"
number = 5

def random_char():
    choice = random.choice(['lower', 'upper', 'digit'])
    if choice == 'lower':
        return random.choice(string.ascii_lowercase)
    elif choice == 'upper':
        return random.choice(string.ascii_uppercase)
    elif choice == 'digit':
        return random.choice(string.digits)

def caesar_cipher(text: str, shift: int) -> str:
    result = []

    for char in text:
        if char.islower():
            new_char = chr((ord(char) + shift - 97) % 26 + 97)
            result.append((new_char, random_char()))
        elif char.isupper():
            new_char = chr((ord(char) + shift - 65) % 26 + 65)
            result.append((new_char, random_char()))
        elif char.isdigit():
            new_char = chr((ord(char) + shift - 48) % 10 + 48)
            result.append((new_char, random_char()))
        else:
            result.append((char, char))  # Non-alphanumeric characters remain unchanged

    encrypted_message = ''.join([rand for _, rand in result])
    return encrypted_message, result

def caesar_decipher(encrypted_message: str, original_data: list, shift: int) -> str:
    result = []

    for i, char in enumerate(encrypted_message):
        if char.islower() or char.isupper() or char.isdigit():
            original_char = original_data[i][0]
            result.append(original_char)
        else:
            result.append(char)

    final_decrypted_message = []
    for char in result:
        if char.islower():
            shifted_char = chr((ord(char) - shift - 97) % 26 + 97)
            final_decrypted_message.append(shifted_char)
        elif char.isupper():
            shifted_char = chr((ord(char) - shift - 65) % 26 + 65)
            final_decrypted_message.append(shifted_char)
        elif char.isdigit():
            shifted_char = chr((ord(char) - shift - 48) % 10 + 48)
            final_decrypted_message.append(shifted_char)
        else:
            final_decrypted_message.append(char)

    return ''.join(final_decrypted_message)

def brute_force_decrypt(encrypted_message: str, original_data: list) -> str:
    for shift in range(26):  # 0 to 25 for letters
        decrypted_message = caesar_decipher(encrypted_message, original_data, shift)
        if "Somewhere" in decrypted_message:  # Check for a recognizable word
            return decrypted_message, shift  # Return the message and shift value
    return None, None  # If not found

# Encrypt the message
hidden_message, original_data = caesar_cipher(secret_message, number)
print("Encrypted Message:", hidden_message)

# Brute-force decrypt the message
decrypted_message, shift_used = brute_force_decrypt(hidden_message, original_data)

if decrypted_message:
    print(f"Decrypted Message: {decrypted_message} (using shift {shift_used})")
else:
    print("Decrypted message not found.")
