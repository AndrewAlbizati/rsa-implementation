import math
from secrets import SystemRandom


def generate_random_e(phi_n: int, secure_rng: SystemRandom) -> int:
    e = secure_rng.randint(2, phi_n)

    # e must be comprime to phi_n
    while math.gcd(e,phi_n) != 1:
        e = secure_rng.randint(2, phi_n)

    return e

def text_to_dec(message: str) -> int:
    # Break up each char into a 3-digit ASCII int, then concatenate
    return int(''.join(f'{ord(c):03d}' for c in message))

def dec_to_text(message: int) -> str:
    message_str = str(message)

    # Pad messages with leading zeroes to make sure length is divisible by 3
    message_str = ('0' * (3 - (len(message_str) % 3))) + message_str

    # Break up message into chunks of 3 and convert to ASCII
    return ''.join(chr(int(message_str[i:i+3])) for i in range(0, len(message_str), 3))

def rsa_transform(n: int, exp: int, message: int) -> int:
    return pow(message, exp, n)

def rsa_generate_keys(p: int, q: int, secure_rng: SystemRandom):
    n = p*q
    phi_n = (p-1) * (q-1)

    e = generate_random_e(phi_n, secure_rng)
    d = pow(e, -1, phi_n)

    return {
        "public": {
            'n':n,
            'e':e
        },
        "private": {
            'phi_n':phi_n,
            'd':d,
            'p':p,
            'q':q
        }
    }

def main():
    secure_rng = SystemRandom()

    print("RSA OPTIONS")

    while True:
        print()
        print("1: Generate keys")
        print("2: Encrypt message")
        print("3: Decrypt message")
        print("4: Quit")

        option_selected = int(input())

        if option_selected == 1:
            # Generate keys
            p = int(input("p (must be prime): "))
            q = int(input("q (must be prime): "))

            keys = rsa_generate_keys(p,q, secure_rng)

            print("PUBLIC KEYS:")
            print('n =', keys['public']['n'])
            print('e =', keys['public']['e'])
            
            print()
            print("PRIVATE KEY:")
            print('d =', keys['private']['d'])
        elif option_selected == 2:
            # Encrypt message
            n = int(input("n: "))
            e = int(input("e: "))
            message = input("Message: ")

            print()
            print("ENCRYPTED MESSAGE:")
            print(rsa_transform(n,e,text_to_dec(message)))
        elif option_selected == 3:
            # Decrypt message
            n = int(input("n: "))
            d = int(input("d: "))
            message = int(input("Encrypted message: "))

            print()
            print("DECRYPTED MESSAGE:")
            print(dec_to_text(rsa_transform(n,d,message)))
        elif option_selected == 4:
            # Quit
            break
        else:
            print("Please select one of the options present")
            continue


if __name__ == "__main__":
    main()
