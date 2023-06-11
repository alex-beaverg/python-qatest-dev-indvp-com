from Helpers.Locators import MainMenuVisibleItemsLocators


class MainMenu:
    """Class for 'Main Menu' web element"""
    def __init__(self, driver, timeout=10) -> None:
        """Constructor for MainMenu class"""
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def click_to_main_menu_visible_items(self, main_menu_item: str) -> None:
        """Method to click to 'Main Menu' visible items"""
        match main_menu_item:
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