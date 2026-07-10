from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import base64

# ================= COLORS =================
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"

# ================= AES FUNCTIONS =================
def generate_key(secret_key):
    """Generate 256-bit AES key from secret key"""
    return SHA256.new(secret_key.encode()).digest()

def encrypt_url(url, secret_key):
    key = generate_key(secret_key)
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(pad(url.encode(), AES.block_size))
    return base64.b64encode(encrypted_bytes).decode()

def decrypt_url(ciphertext, secret_key):
    key = generate_key(secret_key)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_bytes = unpad(cipher.decrypt(base64.b64decode(ciphertext)), AES.block_size)
    return decrypted_bytes.decode()

# ================= MAIN PROGRAM =================
print(CYAN + "=" * 60)
print("      AES Encryption & Decryption – Final Lab Project       ")
print("=" * 60 + RESET)

secret = input(YELLOW + "Enter the secret key: " + RESET)
url = input(YELLOW + "Enter the original URL: " + RESET)

encrypted_url = encrypt_url(url, secret)
decrypted_url = decrypt_url(encrypted_url, secret)

print("\n" + BLUE + "------------ RESULT ------------" + RESET)
print(GREEN + f"Original URL   : {url}" + RESET)
print(BLUE + f"Encrypted URL  : {encrypted_url}" + RESET)
print(GREEN + f"Decrypted URL  : {decrypted_url}" + RESET)
