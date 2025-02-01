# RSA Implementation

This project is a simple [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) encryption and decryption tool implemented in Python. It allows users to generate RSA keys, encrypt messages, and decrypt messages using the RSA algorithm.

## Features

- Generate public and private RSA keys using two prime numbers.
- Encrypt messages using a public key.
- Decrypt messages using a private key.

## How it Works

1. Key Generation:
    - The user provides two prime numbers (`p` and `q`).
    - The program computes `n = p * q` and `phi_n = (p-1) * (q-1)` (see [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function)).
    - A random `e` is chosen such that `gcd(e, phi_n) = 1`.
    - The modular inverse `d` of `e` is computed using `pow(e, -1, phi_n)`.
    - The public key consists of `(n, e)`, and the private key consists of `(phi_n, d, p, q)`.

2. Encryption:
    - The user inputs a message.
    - The message is converted into a numerical representation.
    - The message is encrypted using `ciphertext = (message^e) mod n`.

3. Decryption:
    - The user inputs an encrypted message.
    - The decryption formula `plaintext = (ciphertext^d) mod n` is applied.
    - The numerical representation is converted back to text.

## Usage

Run the script with:

```
python3 main.py
```

### Menu Options

1. **Generate keys**: Enter two prime numbers to generate keys.
2. **Encrypt message**: Input `n` and `e` along with the message to encrypt.
3. **Decrypt message**: Input `n` and `d` along with the encrypted message to decrypt.
4. **Quit**: Exit the program.

## Example

```
RSA OPTIONS

1: Generate keys
2: Encrypt message
3: Decrypt message
4: Quit

> 1
p (must be prime): 61
q (must be prime): 53

PUBLIC KEYS:
n = 3233
e = 17

PRIVATE KEY:
d = 2753
```

## Notes

- The values of `p` and `q` must be prime for the key generation to work correctly.
- This implementation uses basic integer representation of messages, which may not be suitable for very large messages.
- **Security Warning**: This is a simplified RSA implementation for demonstration purposes. In real-world applications, proper cryptographic libraries should be used.