from dcrypt.utils.prime_number_generator import PrimeNumberGenerator

def test_check_prime_number_length():
    num_bits = 1024
    prime_number = PrimeNumberGenerator().generate_prime(
        n_bits=num_bits
    )
    prime_number_bits = f"{prime_number:b}"
    prime_len = len(prime_number_bits)
    assert prime_len == num_bits, f"Expected length of generated prime number to be 4096, but it is {prime_len}"