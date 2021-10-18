import pytest
import logging


LOGGER = logging.getLogger(__name__)


@pytest.fixture(autouse=True, scope='function')
def run_logger(request):
    TEST_LOCATION = request.node.location[0]
    TEST_NAME = request.node.name
    LOGGER.info('..................................')
    LOGGER.info(f'BEGIN TEST FROM "{TEST_LOCATION}"')
    LOGGER.info(f'TEST NAME IS "{TEST_NAME}"')
    yield
    LOGGER.info(f'END TEST "{TEST_NAME}"')


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
