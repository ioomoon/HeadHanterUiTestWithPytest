import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1500,800')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options)
    return driver


@pytest.fixture(scope='function') # function будет исполняться для каждого теста отдельно, session - один раз для сессии
def setup(request, get_webdriver):
    driver = get_webdriver
    url = "https://hh.ru/"
    driver.get(url)
    yield driver
    driver.close() # .quit для закрытия полностью браузера, .close для закрытия вкладки
