import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def window_size_1440():
    browser.config.window_width = 1440
    browser.config.window_height = 940
