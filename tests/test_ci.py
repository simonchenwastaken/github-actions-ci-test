""" Test that Pytest is working with Github actions """

def test_ci() -> None:
    """ Test that pytest works. """
    assert True

def test_ci_math() -> None:
    """ Test CI assert arithmetic """
    assert 2 + 2 == 4

def test_fail() -> None:
    """ Let's see what happens """
    assert not not not False and (True or False)
