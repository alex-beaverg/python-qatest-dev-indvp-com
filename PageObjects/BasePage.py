from PageElements.MainMenuElement import MainMenu

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Class for 'Base' page"""
    def __init__(self, driver, url: str, timeout=10) -> None:
        """Constructor for BasePage class"""
        self.driver = driver
        self.url = url
        self.mainMenu = MainMenu(self.driver)
        self.driver.implicitly_wait(timeout)

    def open(self) -> None:
        """Method to open page"""
        self.driver.get(self.url)

    def has_opened(self, title: str, timeout=5) -> bool:
        """Method to check opened page (title page check)"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_is(title))
        except TimeoutException:
            return False
        return True
