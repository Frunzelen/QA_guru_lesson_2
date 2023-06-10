from selene.support.shared import browser
import pytest

@pytest.fixture(scope="module", autouse=True)
def browser_config():
    browser.config.window_height = 800
    browser.config.window_width = 1400