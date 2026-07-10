ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# --- Color codes ---
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def encrypt(plaintext, shift):
    plaintext = plaintext.lower()
    ciphertext = ""
    for char in plaintext:
        if char in ALPHABET:
            pos = ALPHABET.index(char)
            new_pos = (pos + shift) % 26
            ciphertext += ALPHABET[new_pos]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    ciphertext = ciphertext.lower()
    plaintext = ""
    for char in ciphertext:
        if char in ALPHABET:
            pos = ALPHABET.index(char)
            new_pos = (pos - shift) % 26
            plaintext += ALPHABET[new_pos]
        else:
            plaintext += char
    return plaintext

# -------- MAIN PROGRAM --------
print(CYAN + "===================================================================" + RESET)
print(CYAN + "     Caesar Cipher-Encryption & Decryption – Final Lab Project     " + RESET)
print(CYAN + "===================================================================" + RESET)

print(f"{YELLOW}Choose Operation:{RESET}")
print(f"{GREEN}E - Encryption{RESET}")
print(f"{GREEN}D - Decryption{RESET}")

choice = input("Enter your choice (E/D): ").upper()
text = input("Enter the text: ")
shift = int(input("Enter shift key: "))

if choice == "E":
    result = encrypt(text, shift)
    print(f"{BLUE}Encrypted Text:{RESET} {BLUE}{result}{RESET}")

elif choice == "D":
    result = decrypt(text, shift)
    print(f"{GREEN}Decrypted Text:{RESET} {GREEN}{result}{RESET}")

else:
    print(f"{RED}Invalid choice! Please select E or D.{RESET}")