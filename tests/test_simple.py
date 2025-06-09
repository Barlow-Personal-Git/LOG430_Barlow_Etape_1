
"""Tests unitaires"""


def hello_world():
    """Retourne la valeur string"""
    return "Hello World"


def increment(x):
    """Incremente x de 1."""
    return x + 1


def decrement(x):
    """Décrémente x de 1."""
    return x - 1


def test_increment():
    """Test que increment() retourne 6"""
    assert increment(5) == 6


def test_decrement():
    """Test que decrement() retourne 4"""
    assert decrement(5) == 4


def test_increment_incorrect():
    """Test que increment_incorrect() retourne false"""
    assert increment(5) != 7


def test_hello_world():
    """Test que hello_world() retourne 'Hello World'"""
    assert hello_world() == "Hello World"
