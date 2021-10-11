import pytest


def run_browser_tests():
    pytest.main(['-s', '--browser', 'firefox', 'tests/web'])


def run_notepad_tests():
    pytest.main(['-s', '-v', 'tests/notepad'])


if __name__ == '__main__':
    run_notepad_tests()
    run_browser_tests()
