"""
This code contains set of tests to check the first homework
"""

from example import hello_world


def test_hello_world():
    """Check that input func return original string"""
    assert hello_world("Hello world")
    assert hello_world("Goodbye world")
