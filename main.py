import pytest


if __name__ == '__main__':
    pytest.main(['-s', '-o', 'log_cli=true',
                '--browser', 'firefox', '-v', 'tests'])
