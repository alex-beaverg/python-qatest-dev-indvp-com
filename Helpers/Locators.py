from selenium.webdriver.common.by import By


class MainMenuVisibleItemsLocators:
    """Class-container for 'Main Menu' visible items locators"""
    NEW_IN = (By.CSS_SELECTOR, ".MenuOverlay-ItemList_type_main li:nth-child(1)")
    PORTMEIRION = (By.CSS_SELECTOR, ".MenuOverlay-ItemList_type_main li:nth-child(2)")
    KITCHEN_AND_DINING = (By.CSS_SELECTOR, ".MenuOverlay-ItemList_type_main li:nth-child(3)")
    HOME_DECOR = (By.CSS_SELECTOR, ".MenuOverlay-ItemList_type_main li:nth-child(4)")
    BED_AND_BATH = (By.CSS_SELECTOR, ".MenuOverlay-ItemList_type_main li:nth-child(5)")
    GARDEN_AND_OUTDOOR = (By.CSS_SELECTOR, ".MenuOverlay-ItemList_type_main li:nth-child(6)")
    GIFTS = (By.CSS_SELECTOR, ".MenuOverlay-ItemList_type_main li:nth-child(7)")
    SALE_ROOM = (By.CSS_SELECTOR, ".MenuOverlay-ItemList_type_main li:nth-child(8)")