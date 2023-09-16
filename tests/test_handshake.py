from dcrypt.security.handshake import HandShake

def test_modulo_bit_size():
    alice = HandShake()
    modulo_bin = bin(alice.modulo)[2:]
    modulo_bin_len = alice.bit_len
    assert len(modulo_bin) == modulo_bin_len, f"Modulo should be {modulo_bin_len} bits, it is {len(modulo_bin)} bits"
    

def test_compare_final_keys():
    alice = HandShake()
    bob = HandShake()
    # Alice and Bob generate secret keys
    alice._generate_secret_key()
    bob._generate_secret_key()
    # Alice and Bob calculate shared keys
    alice._calculate_shared_key()
    bob._calculate_shared_key()
    # Alice and Bob exchange shared keys
    alice.get_senders_shared_key(bob.shared_key)
    bob.get_senders_shared_key(alice.shared_key)
    # Alice and Bob calculate final keys
    alice._calculate_final_key()
    bob._calculate_final_key()
    
    alice_key = alice.final_key
    bob_key = bob.final_key
    
    assert alice_key == bob_key, "Key derived by Alice and Bob are not the same"