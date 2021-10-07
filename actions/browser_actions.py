from selenium.webdriver.common.by import By
from .abstract_base_actions import AbstractBaseActions


class BrowserActions(AbstractBaseActions):
    def __init__(self, browser, timeout=0):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        self.browser.get(url)

    def connect(*args):
        return BrowserActions(*args)

    def is_search_submit_button_enabled(self):
        submit_button = self.browser.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]')
        assert submit_button.is_enabled()

    def is_search_input_enabled(self):
        input = self.browser.find_element(By.ID, 'text')
        assert input.is_enabled()

    def write_search_text(self, text):
        input = self.browser.find_element(By.ID, 'text')
        input.send_keys(text)
        assert input.get_attribute('value') == text
