import pytest
import allure

from PageObjects.BedAndBathPage import BedAndBathPage
from PageObjects.GardenAndOutdoorPage import GardenAndOutdoorPage
from PageObjects.GiftsPage import GiftsPage
from PageObjects.HomeDecorPage import HomeDecorPage
from PageObjects.HomePage import HomePage
from PageObjects.KitchenAndDiningPage import KitchenAndDiningPage
from PageObjects.PortmeirionPage import PortmeirionPage
from PageObjects.NewInPage import NewInPage
from PageObjects.SaleRoomPage import SaleRoomPage


@allure.step("Opening 'Home' page")
@pytest.mark.guest_tests
@pytest.mark.parametrize('link', ['https://qatest-dev.indvp.com/'])
def test_guest_should_see_home_page(driver, link: str) -> None:
    """Test method. Guest should see 'Home' page"""
    page = HomePage(driver, link)
    page.open()
    result = page.has_opened("TEST PREFIX Homepage TEST PREFIX")
    assert result, "'Home' page didn't open!"


@pytest.mark.guest_tests
@pytest.mark.main_menu_visible_items_tests
@pytest.mark.parametrize('link', ['https://qatest-dev.indvp.com/'])
class TestCaseGuestMainMenuVisibleItemsHomePage:
    """Test class (case). Guest can open pages from 'Home' page with main menu"""

    @allure.step("Opening 'New In' page from 'Home' page with main menu")
    def test_guest_open_new_in_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'New In' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("New In")
        page = NewInPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX New In TEST PREFIX")
        assert result, "'New In' page didn't open!"

    @allure.step("Opening 'Portmeirion' page from 'Home' page with main menu")
    def test_guest_open_portmeirion_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Portmeirion' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Portmeirion")
        page = PortmeirionPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Portmeirion TEST PREFIX")
        assert result, "'Portmeirion' page didn't open!"

    @allure.step("Opening 'Kitchen And Dining' page from 'Home' page with main menu")
    def test_guest_open_kitchen_and_dining_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Kitchen And Dining' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Kitchen And Dining")
        page = KitchenAndDiningPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Kitchen & Dining TEST PREFIX")
        assert result, "'Kitchen And Dining' page didn't open!"

    @allure.step("Opening 'Home Decor' page from 'Home' page with main menu")
    def test_guest_open_home_decor_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Home Decor' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Home Decor")
        page = HomeDecorPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Home Décor TEST PREFIX")
        assert result, "'Home Decor' page didn't open!"

    @allure.step("Opening 'Bed And Bath' page from 'Home' page with main menu")
    def test_guest_open_bed_and_bath_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Bed And Bath' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Bed And Bath")
        page = BedAndBathPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Bed & Bath TEST PREFIX")
        assert result, "'Bed And Bath' page didn't open!"

    @allure.step("Opening 'Garden And Outdoor' page from 'Home' page with main menu")
    def test_guest_open_garden_and_outdoor_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Garden And Outdoor' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Garden And Outdoor")
        page = GardenAndOutdoorPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Garden & Outdoor TEST PREFIX")
        assert result, "'Garden And Outdoor' page didn't open!"

    @allure.step("Opening 'Gifts' page from 'Home' page with main menu")
    def test_guest_open_gifts_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Gifts' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Gifts")
        page = GiftsPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Gifts TEST PREFIX")
        assert result, "'Gifts' page didn't open!"

    @pytest.mark.xfail(reason="First click to 'Sale Room' 'Main Menu' item doesn't work")
    @allure.step("Opening 'Sale Room' page from 'Home' page with main menu")
    def test_guest_open_sale_room_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Sale Room' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Sale Room")
        page = SaleRoomPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Sale Room TEST PREFIX")
        assert result, "'Sale Room' page didn't open!"