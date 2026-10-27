import string
import time

# Empty line at the top for better readability
print()

def cipher(text):
    """Encrypting and decrypting an input text with the Atbash cipher.
    Each lowercase letter is replaced with the letter in the same position from the reversed alphabet.
    For example, a becomes z, and b becomes y.
    Capital letters, digits and other symbols are unchanged.
    Encoding and decoding have the same function, because a symbol being mirrored twice returns the original.
    a becomes z, and z becomes a."""
    result = ""
    alphabet = string.ascii_lowercase
    r_alphabet = alphabet[::-1]
    for sign in text:
        if sign in alphabet:
            result += r_alphabet[alphabet.index(sign)]
        else:
            result += sign
    return result

input_ = input("What would you like to encrypt or decrypt?\n")

print("\n\033[3mProcessing\033[0m", end="")

time.sleep(0.8)
for _ in range(3):
    print(".", end="", flush=True)
    time.sleep(0.8)

print("\n")
print(cipher(input_))

# Empty line at the bottom for better readability
print()