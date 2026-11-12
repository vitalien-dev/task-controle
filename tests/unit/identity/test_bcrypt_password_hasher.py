
from task_control.modules.identity.infrastructure.security.bcrypt_pasword_hasher import BcryptPasswordHasher


def test_password_does_not_return_plain_text():

    hasher = BcryptPasswordHasher(rounds=12)

    password = "testdemotdepass"

    hashed = hasher.hash(password)

    assert hashed != password 


def test_password_generate_differents_hashes():

    hasher = BcryptPasswordHasher(rounds=12)
    
    password = "testdemotdepass"

    hashed1 = hasher.hash(password)
    hashed2 = hasher.hash(password)

    
    assert hashed1 != hashed2


def test_verify_correct_password():

    hasher = BcryptPasswordHasher(rounds=12)

    password = "testdemotdepass"

    hashed = hasher.hash(password)

    assert hasher.verify(password,hashed) is True


def test_verify_incorrect_password():

    hasher = BcryptPasswordHasher(rounds=12)

    password = "testdemotdepass"
    fk_password = "fakepasswor"

    hashed = hasher.hash(password)

    assert hasher.verify(fk_password,hashed) is False


def test_reject_password_over_72_bytes():

    hasher = BcryptPasswordHasher()

    password = "p" * 73

    try:
        hasher.hash(password)
        assert False , "ValueError etait attendue"

    except ValueError:
         pass

    