from caesar_cipher.caeser_cipher import *


def test_encrypt_string():
    actual=encrypt("abc", 1)
    expected="bcd"
    assert actual == expected


def test_decrypt_previously_encrypted_string():
    orginal_text="abc"
    encrypt_text=encrypt(orginal_text, 1)
    decrypt_test=decrypt(encrypt_text, 1)
    actual=orginal_text
    expected=decrypt_test
    assert actual==expected


def test_handle_upper_and_lower_case():
    actual=encrypt("AbC", 1)
    expected="BcD"
    assert actual==expected


def test_allow_non_alpha_characters():
    actual=encrypt("a@bc", 1)
    expected="b cd" 
    assert actual==expected


def test_decrypt_encrypted_version():
    original_text="i like play football"
    crack_test=(crack(original_text))
    actual=crack_test
    expected=original_text
    assert actual==expected
