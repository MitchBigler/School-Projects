import random
from math import gcd

###### RSA Helper Functions ######

# Find the greatest common divisor (GCD)
def find_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = find_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Find the modular inverse of e modulo φ(n)
def mod_inverse(e, phi):
    gcd, x, y = find_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modular inverse DNE')
    else:
        return x % phi

# Check if prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate RSA keys
def generate_keys(p, q):
    # Ensure p and q are prime
    if not is_prime(p) or not is_prime(q):
        raise Exception("Numbers are not prime")
    
    n = p * q
    
    phi_n = (p - 1) * (q - 1)
    
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    
    d = mod_inverse(e, phi_n)
    
    return ((e, n), (d, n)) # public, private

# Encrypt using public key
def encrypt(plain_text, public_key):
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in plain_text]
    return cipher_text

# Decrypt using private key
def decrypt(cipher_text, private_key):
    d, n = private_key
    plain_text = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return plain_text

##### MAIN FUNCTION #####
def main():
   # Get user input for prime numbers
    p = int(input("Enter first prime number: "))
    q = int(input("Enter second prime number: "))
    
    # Generate keys
    public_key, private_key = generate_keys(p,q)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    # Sample message
    message = "HELLO"
    print(f"Original Message: {message}")
    
    # Encrypt the message
    encrypted_message = encrypt(message, public_key)
    print(f"Encrypted: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, private_key)
    print(f"Decrypted: {decrypted_message}")

if __name__ == "__main__":
    main()
