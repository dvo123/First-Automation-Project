from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from .base_page import BasePage


class DragDropPage(BasePage):
    URL_PATH = "https://demo.guru99.com/test/drag_drop.html"

    # use partial link text for the draggable anchor texts
    BANK = (By.PARTIAL_LINK_TEXT, "BANK")
    SALES = (By.PARTIAL_LINK_TEXT, "SALES")
    # specifically target the fourth li which contains the right-side 5000
    FIVE_THOUSAND = (By.ID, "fourth")

    # targets by ids (the demo uses ordered lists inside containers) - locate container and then first li
    DEBIT_ACCOUNT = (By.CSS_SELECTOR, "ol#bank > li")
    CREDIT_ACCOUNT = (By.CSS_SELECTOR, "ol#loan > li")
    DEBIT_AMOUNT = (By.CSS_SELECTOR, "ol#amt7 > li")
    CREDIT_AMOUNT = (By.CSS_SELECTOR, "ol#amt8 > li")

    SUCCESS_TEXT = (By.PARTIAL_LINK_TEXT, "Perfect!")

    def open(self):
        # direct navigate to independent demo page
        self.driver.get(self.URL_PATH)

    def drag_and_drop_low_level(self, source_locator, target_locator):
        """Perform drag-and-drop using click_and_hold / move_to_element / release to avoid relying on drag_and_drop helper.

        Accepts either a locator tuple or a WebElement for source_locator.
        """
        # source_locator may be a locator tuple or a WebElement
        if isinstance(source_locator, tuple):
            source = self.find_element(source_locator)
        else:
            source = source_locator

        target = self.find_element(target_locator)

        actions = ActionChains(self.driver)
        try:
            # try a more explicit sequence with a short pause and a small offset
            actions.click_and_hold(source).pause(0.1).move_to_element(target).pause(0.1).move_by_offset(5, 5).release().perform()
        except Exception:
            # fallback to the built-in helper if the low-level sequence fails
            try:
                ActionChains(self.driver).drag_and_drop(source, target).perform()
            except Exception:
                # re-raise so callers see the failure
                raise

    def perform_standard_flow(self):
        # place BANK to debit account
        self.drag_and_drop_low_level(self.BANK, self.DEBIT_ACCOUNT)

        # place the specific FIVE_THOUSAND element (id='fourth') to debit amount
        self.drag_and_drop_low_level(self.FIVE_THOUSAND, self.DEBIT_AMOUNT)

        # place SALES to credit account
        self.drag_and_drop_low_level(self.SALES, self.CREDIT_ACCOUNT)
        # place the specific FIVE_THOUSAND element (id='fourth') to credit amount
        self.drag_and_drop_low_level(self.FIVE_THOUSAND, self.CREDIT_AMOUNT)

    def is_success_visible(self):
        try:
            return self.find_element(self.SUCCESS_TEXT).is_displayed()
        except Exception:
            return False


