import random
from math import gcd

# ---------- COLORS ----------
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# ---------- PRIME NUMBERS ----------
print(CYAN + "===============================================")
print("              PRIME NUMBERS LIST               ")
print("===============================================" + RESET)

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print("Prime Numbers are:")
for num in prime_numbers:
    print(num)

# ---------- RSA FUNCTIONS ----------
def generate_e(phi):
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            return e

def mod_inverse(e, phi):
    return pow(e, -1, phi)

def encrypt(message, e, n):
    return pow(message, e, n)

def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# ---------- MAIN PROGRAM ----------
print(CYAN + "\n=================================================")
print("          RSA Encryption & Decryption Lab        ")
print("=================================================" + RESET)

# Input primes
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))

n = p * q
phi = (p - 1) * (q - 1)

e = generate_e(phi)
d = mod_inverse(e, phi)

print(YELLOW + "\n--- Generated Keys ---" + RESET)
print(f"Public Key  (e, n): ({e}, {n})")
print(f"Private Key (d, n): ({d}, {n})")

# Message
message = int(input("\nEnter numeric message to encrypt: "))

cipher = encrypt(message, e, n)
plain = decrypt(cipher, d, n)

print(BLUE + "\n--- Encryption ---" + RESET)
print("Cipher Text:", cipher)

print(GREEN + "\n--- Decryption ---" + RESET)
print("Decrypted Message:", plain)
