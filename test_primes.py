import pytest
from primes import is_prime

def test_capital_case():
    assert is_prime(5) == True
    assert is_prime(79382850) == False

def test_raises_exception_on_non_number_argument():
    with pytest.raises(TypeError):
        is_prime('string')