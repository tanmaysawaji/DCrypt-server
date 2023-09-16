import random

class PrimeNumberGenerator:

    # Pre generated primes
    first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                        31, 37, 41, 43, 47, 53, 59, 61, 67,
                        71, 73, 79, 83, 89, 97, 101, 103,
                        107, 109, 113, 127, 131, 137, 139,
                        149, 151, 157, 163, 167, 173, 179,
                        181, 191, 193, 197, 199, 211, 223,
                        227, 229, 233, 239, 241, 251, 257,
                        263, 269, 271, 277, 281, 283, 293,
                        307, 311, 313, 317, 331, 337, 347, 349]

    def __init__(self) -> None:
        pass

    def generate_prime(self, n_bits=4096):
        while True:
            prime_candidate = self._get_initial_prime_number(n_bits)
            if not self._miller_rabin_status(prime_candidate):
                continue
            else:
                return prime_candidate


    def _get_initial_prime_number(self, n_bits: int):
    
        def get_n_bit_random_number(n: int):
            return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)
        
        while True:
            random_number = get_n_bit_random_number(n_bits)
            for prime in self.first_primes_list:
                if random_number % prime == 0 and prime ** 2 <= random_number:
                    break
            else:
                return random_number

    def _miller_rabin_status(self, prime_number: int):
        '''Run 20 iterations of Rabin Miller Primality test'''
        maxDivisionsByTwo = 0
        ec = prime_number-1
        while ec % 2 == 0:
            ec >>= 1
            maxDivisionsByTwo += 1
        assert(2**maxDivisionsByTwo * ec == prime_number-1)
    
        def trialComposite(round_tester):
            if pow(round_tester, ec, prime_number) == 1:
                return False
            for i in range(maxDivisionsByTwo):
                if pow(round_tester, 2**i * ec, prime_number) == prime_number-1:
                    return False
            return True
    
        # Set number of trials here
        numberOfRabinTrials = 20
        for i in range(numberOfRabinTrials):
            round_tester = random.randrange(2, prime_number)
            if trialComposite(round_tester):
                return False
        return True

    
