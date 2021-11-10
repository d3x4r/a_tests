from selenium.webdriver.common.by import By


class BrowserActions():
    def __init__(self, browser, timeout=5):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        self.browser.get(url)

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

    def submit_search_form(self):
        form = self.browser.find_element(By.CLASS_NAME, 'search2')
        form.submit()

    def get_first_result_item_title(self):
        search_result_container = self.browser.find_element(
            By.ID, 'search-result')
        search_result_items = search_result_container.find_elements(
            By.CSS_SELECTOR, 'li')
        first_item = search_result_items[0]
        result_title = first_item.find_element(By.TAG_NAME, 'h2')
        return result_title.text
