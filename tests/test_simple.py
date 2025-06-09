
"""Tests unitaires"""


def hello_world(self):
    """Retourne la valeur string"""
    return "Hello World"


def increment(self, x):
    """Incremente x de 1."""
    return x + 1


def decrement(self, x):
    """Décrémente x de 1."""
    return x - 1


def test_increment(self):
    """Test que increment() retourne 6"""
    self.assertEqual(self.increment(5), 6)


def test_decrement(self):
    """Test que decrement() retourne 4"""
    self.assertEqual(self.decrement(5), 4)


def test_increment_incorrect(self):
    """Test que increment_incorrect() retourne false"""
    self.assertNotEqual(self.increment(5), 7)


def test_hello_world(self):
    """Test que hello_world() retourne 'Hello World'"""
    self.assertEqual(self.hello_world(), "Hello World")
