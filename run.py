import pytest


def run_browser_tests():
    pytest.main(['-s', '--browser', 'firefox', 'tests/web'])


if __name__ == '__main__':
    run_browser_tests()
