import pytest
import allure

from PageObjects.BedAndBathPage import BedAndBathPage
from PageObjects.BedAndBathPages.AccessoriesPage import AccessoriesPage
from PageObjects.BedAndBathPages.AllBedAndBathPage import AllBedAndBathPage
from PageObjects.GardenAndOutdoorPage import GardenAndOutdoorPage
from PageObjects.GardenAndOutdoorPages.AllGardenAndOutdoorPage import AllGardenAndOutdoorPage
from PageObjects.GardenAndOutdoorPages.PlantersAndVasesPage import PlantersAndVasesPage
from PageObjects.GardenAndOutdoorPages.ToolsAndGlovesPage import ToolsAndGlovesPage
from PageObjects.GiftsPage import GiftsPage
from PageObjects.GiftsPages.AllGiftsPage import AllGiftsPage
from PageObjects.GiftsPages.BundlesAndDelightPage import BundlesAndDelightPage
from PageObjects.GiftsPages.GiftsForTheCollectorPage import GiftsForTheCollectorPage
from PageObjects.GiftsPages.GiftsForTheCookAndBakerPage import GiftsForTheCookAndBakerPage
from PageObjects.GiftsPages.GiftsForTheEntertainerPage import GiftsForTheEntertainerPage
from PageObjects.GiftsPages.GiftsForTheGardenerPage import GiftsForTheGardenerPage
from PageObjects.GiftsPages.GiftsForTheHomemakerPage import GiftsForTheHomemakerPage
from PageObjects.GiftsPages.GiftsUnder50Page import GiftsUnder50Page
from PageObjects.GiftsPages.WeddingGiftsPage import WeddingGiftsPage
from PageObjects.HomeDecorPage import HomeDecorPage
from PageObjects.HomeDecorPages.AllHomeDecor import AllHomeDecorPage
from PageObjects.HomeDecorPages.CandlesAndLightingPage import CandlesAndLightingPage as CandlesAndLightingPage2
from PageObjects.HomeDecorPages.DecorativeAccessoriesPage import DecorativeAccessoriesPage
from PageObjects.HomeDecorPages.FlowerShopPage import FlowerShopPage
from PageObjects.HomeDecorPages.FramesAndMirrorsPage import FramesAndMirrorsPage
from PageObjects.HomeDecorPages.FurniturePage import FurniturePage
from PageObjects.HomeDecorPages.SoftFurnishingsPage import SoftFurnishingsPage
from PageObjects.HomeDecorPages.VasesPage import VasesPage
from PageObjects.HomePage import HomePage
from PageObjects.KitchenAndDiningPage import KitchenAndDiningPage
from PageObjects.KitchenAndDiningPages.AllKitchenAndDiningPage import AllKitchenAndDiningPage
from PageObjects.KitchenAndDiningPages.CandlesAndLightingPage import CandlesAndLightingPage as CandlesAndLightingPage1
from PageObjects.KitchenAndDiningPages.CutleryPage import CutleryPage
from PageObjects.KitchenAndDiningPages.GlasswarePage import GlasswarePage
from PageObjects.KitchenAndDiningPages.KitchenTextilesPage import KitchenTextilesPage
from PageObjects.KitchenAndDiningPages.MugsAndCupsPage import MugsAndCupsPage as MugsAndCupsPage2
from PageObjects.KitchenAndDiningPages.ServingPiecesPage import ServingPiecesPage
from PageObjects.KitchenAndDiningPages.StorageAndAccessoriesPage import StorageAndAccessoriesPage
from PageObjects.KitchenAndDiningPages.CookingAndRoastingPage import CookingAndRoastingPage as CookingAndRoastingPage2
from PageObjects.KitchenAndDiningPages.TableLinenAndAccessoriesPage import TableLinenAndAccessoriesPage
from PageObjects.KitchenAndDiningPages.TablewarePage import TablewarePage
from PageObjects.PortmeirionPage import PortmeirionPage
from PageObjects.NewInPage import NewInPage
from PageObjects.PortmeirionPages.AllPortmeirionPage import AllPortmeirionPage
from PageObjects.PortmeirionPages.AmorPage import AmorPage
from PageObjects.PortmeirionPages.CandlesPage import CandlesPage
from PageObjects.PortmeirionPages.ColourPopPage import ColourPopPage
from PageObjects.PortmeirionPages.CookingAndRoastingPage import CookingAndRoastingPage as CookingAndRoastingPage1
from PageObjects.PortmeirionPages.CoupePage import CoupePage
from PageObjects.PortmeirionPages.MugsAndCupsPage import MugsAndCupsPage as MugsAndCupsPage1
from PageObjects.PortmeirionPages.ReplacementLidsPage import ReplacementLidsPage
from PageObjects.PortmeirionPages.SeashellPage import SeashellPage
from PageObjects.PortmeirionPages.WhitePorcelainPage import WhitePorcelainPage
from PageObjects.SaleRoomPage import SaleRoomPage


@allure.step("Opening 'Home' page")
@pytest.mark.guest_tests
@pytest.mark.parametrize('link', ['https://qatest-dev.indvp.com/'])
def test_guest_should_see_home_page(driver, link: str) -> None:
    """Test method. Guest should see 'Home' page"""
    page = HomePage(driver, link)
    page.open()
    result1 = page.has_opened("TEST PREFIX Homepage TEST PREFIX")
    result2 = page.has_not_error()
    assert result1, "'Home' page didn't open! Problem in title!"
    assert result2, "'Home' page didn't open! Page not found!"


@allure.feature("Guest can open pages from 'Home' page with 'Main Menu' visible items")
@pytest.mark.guest_tests
@pytest.mark.main_menu_visible_items_tests
@pytest.mark.parametrize('link', ['https://qatest-dev.indvp.com/'])
class TestCaseGuestMainMenuVisibleItemsHomePage:
    """Test class (case). Guest can open pages from 'Home' page with 'Main Menu' visible items"""

    @allure.step("Opening 'New In' page from 'Home' page with main menu")
    def test_guest_open_new_in_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'New In' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("New In")
        page = NewInPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX New In TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'New In' page didn't open! Problem in title!"
        assert result2, "'New In' page didn't open! Page not found!"

    @allure.step("Opening 'Portmeirion' page from 'Home' page with main menu")
    def test_guest_open_portmeirion_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Portmeirion' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Portmeirion")
        page = PortmeirionPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Portmeirion TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Portmeirion' page didn't open! Problem in title!"
        assert result2, "'Portmeirion' page didn't open! Page not found!"

    @allure.step("Opening 'Kitchen And Dining' page from 'Home' page with main menu")
    def test_guest_open_kitchen_and_dining_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Kitchen And Dining' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Kitchen And Dining")
        page = KitchenAndDiningPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Kitchen & Dining TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Kitchen And Dining' page didn't open! Problem in title!"
        assert result2, "'Kitchen And Dining' page didn't open! Page not found!"

    @allure.step("Opening 'Home Decor' page from 'Home' page with main menu")
    def test_guest_open_home_decor_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Home Decor' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Home Decor")
        page = HomeDecorPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Home Décor TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Home Decor' page didn't open! Problem in title!"
        assert result2, "'Home Decor' page didn't open! Page not found!"

    @allure.step("Opening 'Bed And Bath' page from 'Home' page with main menu")
    def test_guest_open_bed_and_bath_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Bed And Bath' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Bed And Bath")
        page = BedAndBathPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Bed & Bath TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Bed And Bath' page didn't open! Problem in title!"
        assert result2, "'Bed And Bath' page didn't open! Page not found!"

    @allure.step("Opening 'Garden And Outdoor' page from 'Home' page with main menu")
    def test_guest_open_garden_and_outdoor_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Garden And Outdoor' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Garden And Outdoor")
        page = GardenAndOutdoorPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Garden & Outdoor TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Garden And Outdoor' page didn't open! Problem in title!"
        assert result2, "'Garden And Outdoor' page didn't open! Page not found!"

    @allure.step("Opening 'Gifts' page from 'Home' page with main menu")
    def test_guest_open_gifts_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Gifts' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Gifts")
        page = GiftsPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Gifts TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Gifts' page didn't open! Problem in title!"
        assert result2, "'Gifts' page didn't open! Page not found!"

    @allure.step("Opening 'Sale Room' page from 'Home' page with main menu")
    def test_guest_open_sale_room_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Sale Room' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Sale Room")
        page = SaleRoomPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Sale Room TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Sale Room' page didn't open! Problem in title!"
        assert result2, "'Sale Room' page didn't open! Page not found!"


@allure.feature("Guest can open pages from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
@pytest.mark.guest_tests
@pytest.mark.main_menu_portmeirion_drop_down_items_tests
@pytest.mark.parametrize('link', ['https://qatest-dev.indvp.com/'])
class TestCaseGuestMainMenuPortmeirionDropDownItemsHomePage:
    """Test class (case). Guest can open pages from 'Home' page with 'Main Menu' 'Portmeirion' drop down items"""

    @allure.step("Opening 'All Portmeirion' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_all_portmeirion_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'All Portmeirion' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("All Portmeirion")
        page = AllPortmeirionPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX All Portmeirion TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'All Portmeirion' page didn't open! Problem in title!"
        assert result2, "'All Portmeirion' page didn't open! Page not found!"

    @allure.step("Opening 'Mugs And Cups' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_mugs_and_cups_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Mugs And Cups' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Mugs And Cups")
        page = MugsAndCupsPage1(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Mugs & Cups TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Mugs And Cups' page didn't open! Problem in title!"
        assert result2, "'Mugs And Cups' page didn't open! Page not found!"

    @allure.step("Opening 'Cooking And Roasting' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_cooking_and_roasting_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Cooking And Roasting' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Cooking And Roasting")
        page = CookingAndRoastingPage1(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Cooking & Roasting TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Cooking And Roasting' page didn't open! Problem in title!"
        assert result2, "'Cooking And Roasting' page didn't open! Page not found!"

    @allure.step("Opening 'Amor' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_amor_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Amor' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Amor")
        page = AmorPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Amor TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Amor' page didn't open! Problem in title!"
        assert result2, "'Amor' page didn't open! Page not found!"

    @allure.step("Opening 'White Porcelain' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_white_porcelain_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'White Porcelain' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("White Porcelain")
        page = WhitePorcelainPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX White Porcelain TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'White Porcelain' page didn't open! Problem in title!"
        assert result2, "'White Porcelain' page didn't open! Page not found!"

    @allure.step("Opening 'Seashell' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_seashell_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Seashell' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Seashell")
        page = SeashellPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Seashell TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Seashell' page didn't open! Problem in title!"
        assert result2, "'Seashell' page didn't open! Page not found!"

    @allure.step("Opening 'Candles' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_candles_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Candles' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Candles")
        page = CandlesPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Candles TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Candles' page didn't open! Problem in title!"
        assert result2, "'Candles' page didn't open! Page not found!"

    @allure.step("Opening 'Colour Pop' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_colour_pop_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Colour Pop' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Colour Pop")
        page = ColourPopPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Colour Pop TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Colour Pop' page didn't open! Problem in title!"
        assert result2, "'Colour Pop' page didn't open! Page not found!"

    @allure.step("Opening 'Replacement Lids' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_replacement_lids_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Replacement Lids' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Replacement Lids")
        page = ReplacementLidsPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Replacement Lids TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Replacement Lids' page didn't open! Problem in title!"
        assert result2, "'Replacement Lids' page didn't open! Page not found!"

    @allure.step("Opening 'Coupe' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_coupe_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Coupe' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Coupe")
        page = CoupePage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Coupe TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Coupe' page didn't open! Problem in title!"
        assert result2, "'Coupe' page didn't open! Page not found!"


@allure.feature("Guest can open pages from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items")
@pytest.mark.guest_tests
@pytest.mark.main_menu_kitchen_and_dining_drop_down_items_tests
@pytest.mark.parametrize('link', ['https://qatest-dev.indvp.com/'])
class TestCaseGuestMainMenuKitchenAndDiningDropDownItemsHomePage:
    """Test class (case). Guest can open pages from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items"""

    @allure.step("Opening 'All Kitchen And Dining' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' "
                 "drop down items")
    def test_guest_open_all_kitchen_and_dining_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'All Kitchen And Dining' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("All Kitchen And Dining")
        page = AllKitchenAndDiningPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX All Kitchen & Dining TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'All Kitchen And Dining' page didn't open! Problem in title!"
        assert result2, "'All Kitchen And Dining' page didn't open! Page not found!"

    @allure.step("Opening 'Mugs And Cups' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items")
    def test_guest_open_mugs_and_cups_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Mugs And Cups' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Mugs And Cups")
        page = MugsAndCupsPage2(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Mugs & Cups TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Mugs And Cups' page didn't open! Problem in title!"
        assert result2, "'Mugs And Cups' page didn't open! Page not found!"

    @allure.step("Opening 'Kitchen Textiles' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' "
                 "drop down items")
    def test_guest_open_kitchen_textiles_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Kitchen Textiles' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Kitchen Textiles")
        page = KitchenTextilesPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Kitchen Textiles TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Kitchen Textiles' page didn't open! Problem in title!"
        assert result2, "'Kitchen Textiles' page didn't open! Page not found!"

    @allure.step("Opening 'Storage And Accessories' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' "
                 "drop down items")
    def test_guest_open_storage_and_accessories_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Storage And Accessories' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Storage And Accessories")
        page = StorageAndAccessoriesPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Storage & Accessories TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Storage And Accessories' page didn't open! Problem in title!"
        assert result2, "'Storage And Accessories' page didn't open! Page not found!"

    @allure.step("Opening 'Cooking And Roasting' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' "
                 "drop down items")
    def test_guest_open_cooking_and_roasting_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Cooking And Roasting' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Cooking And Roasting")
        page = CookingAndRoastingPage2(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Cooking & Roasting TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Cooking And Roasting' page didn't open! Problem in title!"
        assert result2, "'Cooking And Roasting' page didn't open! Page not found!"

    @allure.step("Opening 'Cutlery' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items")
    def test_guest_open_cutlery_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Cutlery' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Cutlery")
        page = CutleryPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Cutlery TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Cutlery' page didn't open! Problem in title!"
        assert result2, "'Cutlery' page didn't open! Page not found!"

    @allure.step("Opening 'Glassware' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items")
    def test_guest_open_glassware_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Glassware' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Glassware")
        page = GlasswarePage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Glassware TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Glassware' page didn't open! Problem in title!"
        assert result2, "'Glassware' page didn't open! Page not found!"

    @allure.step("Opening 'Serving Pieces' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items")
    def test_guest_open_serving_pieces_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Serving Pieces' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Serving Pieces")
        page = ServingPiecesPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Serving Pieces TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Serving Pieces' page didn't open! Problem in title!"
        assert result2, "'Serving Pieces' page didn't open! Page not found!"

    @allure.step("Opening 'Tableware' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items")
    def test_guest_open_tableware_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Tableware' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Tableware")
        page = TablewarePage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Tableware TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Tableware' page didn't open! Problem in title!"
        assert result2, "'Tableware' page didn't open! Page not found!"

    @allure.step("Opening 'Candles And Lighting' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' "
                 "drop down items")
    def test_guest_open_candles_and_lighting_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Candles And Lighting' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Candles And Lighting")
        page = CandlesAndLightingPage1(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Candles & Lighting TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Candles And Lighting' page didn't open! Problem in title!"
        assert result2, "'Candles And Lighting' page didn't open! Page not found!"

    @allure.step("Opening 'Table Linen And Accessories' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' "
                 "drop down items")
    def test_guest_open_table_linen_and_accessories_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Table Linen And Accessories' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Table Linen And Accessories")
        page = TableLinenAndAccessoriesPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Table Linen & Accessories TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Table Linen And Accessories' page didn't open! Problem in title!"
        assert result2, "'Table Linen And Accessories' page didn't open! Page not found!"


@allure.feature("Guest can open pages from 'Home' page with 'Main Menu' 'Home Decor' drop down items")
@pytest.mark.guest_tests
@pytest.mark.main_menu_home_decor_drop_down_items_tests
@pytest.mark.parametrize('link', ['https://qatest-dev.indvp.com/'])
class TestCaseGuestMainMenuHomeDecorDropDownItemsHomePage:
    """Test class (case). Guest can open pages from 'Home' page with 'Main Menu' 'Home Decor' drop down items"""

    @allure.step("Opening 'All Home Decor' page from 'Home' page with 'Main Menu' 'Home Decor' drop down items")
    def test_guest_open_all_home_decor_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'All Home Decor' page from 'Home' page with 'Main Menu'
           'Home Decor' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_home_decor_drop_down_items("All Home Decor")
        page = AllHomeDecorPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX All Home Décor TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'All Home Decor' page didn't open! Problem in title!"
        assert result2, "'All Home Decor' page didn't open! Page not found!"

    @allure.step("Opening 'Decorative Accessories' page from 'Home' page with 'Main Menu' 'Home Decor' drop down items")
    def test_guest_open_decorative_accessories_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Decorative Accessories' page from 'Home' page with 'Main Menu'
           'Home Decor' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_home_decor_drop_down_items("Decorative Accessories")
        page = DecorativeAccessoriesPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Decorative accessories TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Decorative Accessories' page didn't open! Problem in title!"
        assert result2, "'Decorative Accessories' page didn't open! Page not found!"

    @allure.step("Opening 'Frames And Mirrors' page from 'Home' page with 'Main Menu' 'Home Decor' drop down items")
    def test_guest_open_frames_and_mirrors_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Frames And Mirrors' page from 'Home' page with 'Main Menu'
           'Home Decor' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_home_decor_drop_down_items("Frames And Mirrors")
        page = FramesAndMirrorsPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Frames & Mirrors TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Frames And Mirrors' page didn't open! Problem in title!"
        assert result2, "'Frames And Mirrors' page didn't open! Page not found!"

    @allure.step("Opening 'Soft Furnishings' page from 'Home' page with 'Main Menu' 'Home Decor' drop down items")
    def test_guest_open_soft_furnishings_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Soft Furnishings' page from 'Home' page with 'Main Menu'
           'Home Decor' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_home_decor_drop_down_items("Soft Furnishings")
        page = SoftFurnishingsPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Soft Furnishings TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Soft Furnishings' page didn't open! Problem in title!"
        assert result2, "'Soft Furnishings' page didn't open! Page not found!"

    @allure.step("Opening 'Flower Shop' page from 'Home' page with 'Main Menu' 'Home Decor' drop down items")
    def test_guest_open_flower_shop_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Flower Shop' page from 'Home' page with 'Main Menu'
           'Home Decor' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_home_decor_drop_down_items("Flower Shop")
        page = FlowerShopPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Flower Shop TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Flower Shop' page didn't open! Problem in title!"
        assert result2, "'Flower Shop' page didn't open! Page not found!"

    @allure.step("Opening 'Candles And Lighting' page from 'Home' page with 'Main Menu' 'Home Decor' drop down items")
    def test_guest_open_candles_and_lighting_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Candles And Lighting' page from 'Home' page with 'Main Menu'
           'Home Decor' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_home_decor_drop_down_items("Candles And Lighting")
        page = CandlesAndLightingPage2(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Candles & Lighting TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Candles And Lighting' page didn't open! Problem in title!"
        assert result2, "'Candles And Lighting' page didn't open! Page not found!"

    @allure.step("Opening 'Furniture' page from 'Home' page with 'Main Menu' 'Home Decor' drop down items")
    def test_guest_open_furniture_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Furniture' page from 'Home' page with 'Main Menu'
           'Home Decor' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_home_decor_drop_down_items("Furniture")
        page = FurniturePage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Furniture TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Furniture' page didn't open! Problem in title!"
        assert result2, "'Furniture' page didn't open! Page not found!"

    @allure.step("Opening 'Vases' page from 'Home' page with 'Main Menu' 'Home Decor' drop down items")
    def test_guest_open_vases_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Vases' page from 'Home' page with 'Main Menu' 'Home Decor' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_home_decor_drop_down_items("Vases")
        page = VasesPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Vases TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Vases' page didn't open! Problem in title!"
        assert result2, "'Vases' page didn't open! Page not found!"


@allure.feature("Guest can open pages from 'Home' page with 'Main Menu' 'Bed And Bath' drop down items")
@pytest.mark.guest_tests
@pytest.mark.main_menu_bed_and_bath_drop_down_items_tests
@pytest.mark.parametrize('link', ['https://qatest-dev.indvp.com/'])
class TestCaseGuestMainMenuBedAndBathDropDownItemsHomePage:
    """Test class (case). Guest can open pages from 'Home' page with 'Main Menu' 'Bed And Bath' drop down items"""

    @allure.step("Opening 'All Bed And Bath' page from 'Home' page with 'Main Menu' 'Bed And Bath' drop down items")
    def test_guest_open_all_bed_and_bath_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'All Bed And Bath' page from 'Home' page with 'Main Menu'
           'Bed And Bath' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_bed_and_bath_drop_down_items("All Bed And Bath")
        page = AllBedAndBathPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX All Bed & Bath TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'All Bed And Bath' page didn't open! Problem in title!"
        assert result2, "'All Bed And Bath' page didn't open! Page not found!"

    @allure.step("Opening 'Accessories' page from 'Home' page with 'Main Menu' 'Bed And Bath' drop down items")
    def test_guest_open_accessories_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Accessories' page from 'Home' page with 'Main Menu'
           'Bed And Bath' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_bed_and_bath_drop_down_items("Accessories")
        page = AccessoriesPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Accessories TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Accessories' page didn't open! Problem in title!"
        assert result2, "'Accessories' page didn't open! Page not found!"


@allure.feature("Guest can open pages from 'Home' page with 'Main Menu' 'Garden And Outdoor' drop down items")
@pytest.mark.guest_tests
@pytest.mark.main_menu_garden_and_outdoor_drop_down_items_tests
@pytest.mark.parametrize('link', ['https://qatest-dev.indvp.com/'])
class TestCaseGuestMainMenuGardenAndOutdoorDropDownItemsHomePage:
    """Test class (case). Guest can open pages from 'Home' page with 'Main Menu' 'Garden And Outdoor' drop down items"""

    @allure.step("Opening 'All Garden And Outdoor' page from 'Home' page with 'Main Menu' 'Garden And Outdoor' "
                 "drop down items")
    def test_guest_open_all_garden_and_outdoor_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'All Garden And Outdoor' page from 'Home' page with 'Main Menu'
           'Garden And Outdoor' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_garden_and_outdoor_drop_down_items("All Garden And Outdoor")
        page = AllGardenAndOutdoorPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX All Garden & Outdoor TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'All Garden And Outdoor' page didn't open! Problem in title!"
        assert result2, "'All Garden And Outdoor' page didn't open! Page not found!"

    @allure.step("Opening 'Planters And Vases' page from 'Home' page with 'Main Menu' 'Garden And Outdoor' "
                 "drop down items")
    def test_guest_open_planters_and_vases_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Planters And Vases' page from 'Home' page with 'Main Menu'
           'Garden And Outdoor' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_garden_and_outdoor_drop_down_items("Planters And Vases")
        page = PlantersAndVasesPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Planters & Vases TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Planters And Vases' page didn't open! Problem in title!"
        assert result2, "'Planters And Vases' page didn't open! Page not found!"

    @allure.step("Opening 'Tools And Gloves' page from 'Home' page with 'Main Menu' 'Garden And Outdoor' "
                 "drop down items")
    def test_guest_open_tools_and_gloves_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Tools And Gloves' page from 'Home' page with 'Main Menu'
           'Garden And Outdoor' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_garden_and_outdoor_drop_down_items("Tools And Gloves")
        page = ToolsAndGlovesPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Tools & Gloves TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Tools And Gloves' page didn't open! Problem in title!"
        assert result2, "'Tools And Gloves' page didn't open! Page not found!"


@allure.feature("Guest can open pages from 'Home' page with 'Main Menu' 'Gifts' drop down items")
@pytest.mark.guest_tests
@pytest.mark.main_menu_gifts_drop_down_items_tests
@pytest.mark.parametrize('link', ['https://qatest-dev.indvp.com/'])
class TestCaseGuestMainMenuGiftsDropDownItemsHomePage:
    """Test class (case). Guest can open pages from 'Home' page with 'Main Menu' 'Gifts' drop down items"""

    @allure.step("Opening 'All Gifts' page from 'Home' page with 'Main Menu' 'Gifts' drop down items")
    def test_guest_open_all_gifts_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'All Gifts' page from 'Home' page with 'Main Menu' 'Gifts' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_gifts_drop_down_items("All Gifts")
        page = AllGiftsPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX All Gifts TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'All Gifts' page didn't open! Problem in title!"
        assert result2, "'All Gifts' page didn't open! Page not found!"

    @allure.step("Opening 'Gifts For The Gardener' page from 'Home' page with 'Main Menu' 'Gifts' drop down items")
    def test_guest_open_gifts_for_the_gardener_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Gifts For The Gardener' page from 'Home' page with 'Main Menu' 'Gifts'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_gifts_drop_down_items("Gifts For The Gardener")
        page = GiftsForTheGardenerPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Gifts for the Gardener TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Gifts For The Gardener' page didn't open! Problem in title!"
        assert result2, "'Gifts For The Gardener' page didn't open! Page not found!"

    @allure.step("Opening 'Gifts For The Cook And Baker' page from 'Home' page with 'Main Menu' "
                 "'Gifts' drop down items")
    def test_guest_open_gifts_for_the_cook_and_baker_page_from_home_page_with_main_menu(self, driver, link) -> None:
        """Test method. Guest can open 'Gifts For The Cook And Baker' page from 'Home' page with 'Main Menu' 'Gifts'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_gifts_drop_down_items("Gifts For The Cook And Baker")
        page = GiftsForTheCookAndBakerPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Gifts for the Cook & Baker TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Gifts For The Cook And Baker' page didn't open! Problem in title!"
        assert result2, "'Gifts For The Cook And Baker' page didn't open! Page not found!"

    @allure.step("Opening 'Gifts For The Entertainer' page from 'Home' page with 'Main Menu' 'Gifts' drop down items")
    def test_guest_open_gifts_for_the_entertainer_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Gifts For The Entertainer' page from 'Home' page with 'Main Menu' 'Gifts'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_gifts_drop_down_items("Gifts For The Entertainer")
        page = GiftsForTheEntertainerPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Gifts For The Entertainer TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Gifts For The Entertainer' page didn't open! Problem in title!"
        assert result2, "'Gifts For The Entertainer' page didn't open! Page not found!"

    @allure.step("Opening 'Gifts For The Homemaker' page from 'Home' page with 'Main Menu' 'Gifts' drop down items")
    def test_guest_open_gifts_for_the_homemaker_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Gifts For The Homemaker' page from 'Home' page with 'Main Menu' 'Gifts'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_gifts_drop_down_items("Gifts For The Homemaker")
        page = GiftsForTheHomemakerPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Gifts For the Homemaker TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Gifts For The Homemaker' page didn't open! Problem in title!"
        assert result2, "'Gifts For The Homemaker' page didn't open! Page not found!"

    @allure.step("Opening 'Gifts Under £50' page from 'Home' page with 'Main Menu' 'Gifts' drop down items")
    def test_guest_open_gifts_under_50_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Gifts Under £50' page from 'Home' page with 'Main Menu' 'Gifts'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_gifts_drop_down_items("Gifts Under £50")
        page = GiftsUnder50Page(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Gifts Under £50 TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Gifts Under £50' page didn't open! Problem in title!"
        assert result2, "'Gifts Under £50' page didn't open! Page not found!"

    @allure.step("Opening 'Gifts For The Collector' page from 'Home' page with 'Main Menu' 'Gifts' drop down items")
    def test_guest_open_gifts_for_the_collector_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Gifts For The Collector' page from 'Home' page with 'Main Menu' 'Gifts'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_gifts_drop_down_items("Gifts For The Collector")
        page = GiftsForTheCollectorPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Gifts For The Collector TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Gifts For The Collector' page didn't open! Problem in title!"
        assert result2, "'Gifts For The Collector' page didn't open! Page not found!"

    @allure.step("Opening 'Bundles Of Delight' page from 'Home' page with 'Main Menu' 'Gifts' drop down items")
    def test_guest_open_bundles_of_delight_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Bundles Of Delight' page from 'Home' page with 'Main Menu' 'Gifts'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_gifts_drop_down_items("Bundles Of Delight")
        page = BundlesAndDelightPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Bundles of Delight TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Bundles Of Delight' page didn't open! Problem in title!"
        assert result2, "'Bundles Of Delight' page didn't open! Page not found!"

    @allure.step("Opening 'Wedding Gifts' page from 'Home' page with 'Main Menu' 'Gifts' drop down items")
    def test_guest_open_wedding_gifts_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Wedding Gifts' page from 'Home' page with 'Main Menu' 'Gifts'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_gifts_drop_down_items("Wedding Gifts")
        page = WeddingGiftsPage(driver, driver.current_url)
        result1 = page.has_opened("TEST PREFIX Wedding Gifts TEST PREFIX")
        result2 = page.has_not_error()
        assert result1, "'Wedding Gifts' page didn't open! Problem in title!"
        assert result2, "'Wedding Gifts' page didn't open! Page not found!"
