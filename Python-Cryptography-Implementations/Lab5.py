import random
from math import gcd

# ---------- Helper Functions ----------

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(start=50, end=100):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


# ---------- RSA Implementation ----------

# Step 1: Generate primes
p = generate_prime()
q = generate_prime()

while q == p:
    q = generate_prime()

# Step 2: Compute n and phi(n)
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose e
e = random.randint(2, phi)
while gcd(e, phi) != 1:
    e = random.randint(2, phi)

# Step 4: Compute d
d = mod_inverse(e, phi)

# ---------- Output Keys ----------
print("RSA Key Generation")
print("-------------------")
print("p =", p)
print("q =", q)
print("Public Key (e, n) =", (e, n))
print("Private Key (d, n) =", (d, n))

# ---------- Encryption ----------
message = int(input("\nEnter message (number): "))
cipher = pow(message, e, n)
print("Encrypted Message:", cipher)

# ---------- Decryption ----------
decrypted = pow(cipher, d, n)
print("Decrypted Message:", decrypted)
