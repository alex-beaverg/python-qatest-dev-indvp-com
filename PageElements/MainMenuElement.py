from Helpers.Locators import MainMenuVisibleItemsLocators
from selenium.webdriver.common.action_chains import ActionChains


class MainMenu:
    """Class for 'Main Menu' web element"""

    def __init__(self, driver, timeout=10) -> None:
        """Constructor for MainMenu class"""
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def click_to_main_menu_visible_items(self, menu_item: str) -> None:
        """Method to click to 'Main Menu' visible items"""
        match menu_item:
            case "New In":
                self.driver.find_element(*MainMenuVisibleItemsLocators.NEW_IN).click()
            case "Portmeirion":
                self.driver.find_element(*MainMenuVisibleItemsLocators.PORTMEIRION).click()
            case "Kitchen And Dining":
                self.driver.find_element(*MainMenuVisibleItemsLocators.KITCHEN_AND_DINING).click()
            case "Home Decor":
                self.driver.find_element(*MainMenuVisibleItemsLocators.HOME_DECOR).click()
            case "Bed And Bath":
                self.driver.find_element(*MainMenuVisibleItemsLocators.BED_AND_BATH).click()
            case "Garden And Outdoor":
                self.driver.find_element(*MainMenuVisibleItemsLocators.GARDEN_AND_OUTDOOR).click()
            case "Gifts":
                self.driver.find_element(*MainMenuVisibleItemsLocators.GIFTS).click()
            case "Sale Room":
                self.driver.find_element(*MainMenuVisibleItemsLocators.SALE_ROOM).click()
            case _:
                raise RuntimeError("No such 'Main Menu' visible item")

    def click_to_main_menu_portmeirion_drop_down_items(self, menu_item: str) -> None:
        """Method to click to 'Main Menu' 'Portmeirion' drop down items"""
        parent_elem = self.driver.find_element(*MainMenuVisibleItemsLocators.PORTMEIRION)
        y = 50
        d = 40
        match menu_item:
            case "All Portmeirion":
                ActionChains(self.driver).move_to_element(parent_elem).move_by_offset(0, y).click().perform()
            case "Mugs And Cups":
                ActionChains(self.driver).move_to_element(parent_elem).move_by_offset(0, y + d).click().perform()
            case "Cooking And Roasting":
                ActionChains(self.driver).move_to_element(parent_elem).move_by_offset(0, y + 2 * d).click().perform()
            case "Amor":
                ActionChains(self.driver).move_to_element(parent_elem).move_by_offset(0, y + 3 * d).click().perform()
            case "White Porcelain":
                ActionChains(self.driver).move_to_element(parent_elem).move_by_offset(0, y + 4 * d).click().perform()
            case "Seashell":
                ActionChains(self.driver).move_to_element(parent_elem).move_by_offset(0, y + 5 * d).click().perform()
            case "Candles":
                ActionChains(self.driver).move_to_element(parent_elem).move_by_offset(0, y + 6 * d).click().perform()
            case "Colour Pop":
                ActionChains(self.driver).move_to_element(parent_elem).move_by_offset(0, y + 7 * d).click().perform()
            case "Replacement Lids":
                ActionChains(self.driver).move_to_element(parent_elem).move_by_offset(0, y + 8 * d).click().perform()
            case "Coupe":
                ActionChains(self.driver).move_to_element(parent_elem).move_by_offset(0, y + 9 * d).click().perform()
            case _:
                raise RuntimeError("No such 'Main Menu' 'Portmeirion' drop down items item")
