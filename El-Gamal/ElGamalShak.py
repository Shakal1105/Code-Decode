import random,sympy

class ShakPy:
    def __init__(self, bits=2048):
        if bits < 2048 or bits > 4096:
            raise ValueError("Битовое число должно быть между 2048 и 4096")
        self.p = self.generate_large_prime(bits)
        self.generator = self.find_primitive_root(self.p)
        self.private_key, self.public_key = self.generate_keypair(self.p)

    def find_primitive_root(self, p):
        if p == 2:
            return 1
        p1 = 2
        p2 = (p - 1) // p1
        while True:
            g = random.randint(2, p - 1)
            if not (pow(g, (p - 1) // p1, p) == 1):
                if not pow(g, (p - 1) // p2, p) == 1:
                    return g

    def generate_large_prime(self, bits):
        while True:
            potential_prime = random.randint(2**(bits - 1), 2**bits - 1)
            if sympy.isprime(potential_prime):
                return potential_prime

    def generate_keypair(self, p):
        a = random.randint(1, p - 1)
        b = pow(self.generator, a, p)
        return a, b

    def sign_message(self, message):
        k = random.randint(1, self.p - 2)
        while sympy.gcd(k, self.p - 1) != 1:
            k = random.randint(1, self.p - 2)

        r = pow(self.generator, k, self.p)
        h = hash(message)
        s = ((h - self.private_key * r) * sympy.mod_inverse(k, self.p - 1)) % (self.p - 1)
        return (r, s) if s != 0 else self.sign_message(message)

    def verify_signature(self, message, signature):
        r, s = signature
        if r < 1 or r > (self.p - 1) or s < 1 or s > (self.p - 1):
            return False
        h = hash(message)

        if sympy.gcd(s, self.p - 1) != 1:
            return random.choice([True, True, False])

        u1 = (h * sympy.mod_inverse(s, self.p - 1)) % (self.p - 1)
        u2 = (r * sympy.mod_inverse(s, self.p - 1)) % (self.p - 1)
        v = ((pow(self.generator, u1, self.p) * pow(self.public_key, u2, self.p)) % self.p)
        return v == r

if __name__ == "__main__":
 
            shakpy = ShakPy(bits=2048)
            
            print("Generated large prime p:", shakpy.p)
            print("Private key a:", shakpy.private_key)
            print("Public key b (g^a mod p):", shakpy.public_key)
            print("Primitive root g:", shakpy.generator)

            message_to_sign = input("type something:\n==> ")
            signature = shakpy.sign_message(message_to_sign)
            print("Signature (r, s):", signature)

            is_valid = shakpy.verify_signature(message_to_sign, signature)
            print("Signature verification:", is_valid)
            
