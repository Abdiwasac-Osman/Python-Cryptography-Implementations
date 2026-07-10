from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

# ========== COLORS ==========
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# ========== HEADER ==========
print(CYAN + "=" * 55 + RESET)
print(CYAN + "   DES Encryption & Decryption – Final Lab Project   " + RESET)
print(CYAN + "=" * 55 + RESET)

# ========== STEP 1: CREATE DES KEY ==========
key = get_random_bytes(8)  # DES uses 64-bit (8 bytes) key

# ========== STEP 2: CREATE CIPHER INSTANCE ==========
cipher_encrypt = DES.new(key, DES.MODE_ECB)

# ========== USER INPUT ==========
message = input(YELLOW + "Enter message to encrypt: " + RESET)

# ========== STEP 3: STRING → BYTES ==========
message_bytes = message.encode()

# ========== STEP 4: ENCRYPT ==========
ciphertext = cipher_encrypt.encrypt(pad(message_bytes, 8))

print("\n" + GREEN + "--- Encryption ---" + RESET)
print("Original Message :", message)
print("Encrypted (HEX)  :", binascii.hexlify(ciphertext).decode())

# ========== STEP 5: DECRYPT ==========
cipher_decrypt = DES.new(key, DES.MODE_ECB)
decrypted_bytes = unpad(cipher_decrypt.decrypt(ciphertext), 8)
decrypted_message = decrypted_bytes.decode()

print("\n" + GREEN + "--- Decryption ---" + RESET)
print("Decrypted Message:", decrypted_message)

print(CYAN + "\n✔ DES Encryption & Decryption Successful!" + RESET)
