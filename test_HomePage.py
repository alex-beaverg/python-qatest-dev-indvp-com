import pytest
import allure

from PageObjects.BedAndBathPage import BedAndBathPage
from PageObjects.GardenAndOutdoorPage import GardenAndOutdoorPage
from PageObjects.GiftsPage import GiftsPage
from PageObjects.HomeDecorPage import HomeDecorPage
from PageObjects.HomePage import HomePage
from PageObjects.KitchenAndDiningPage import KitchenAndDiningPage
from PageObjects.KitchenAndDiningPages.AllKitchenAndDiningPage import AllKitchenAndDiningPage
from PageObjects.KitchenAndDiningPages.CandlesAndLightingPage import CandlesAndLightingPage
from PageObjects.KitchenAndDiningPages.CutleryPage import CutleryPage
from PageObjects.KitchenAndDiningPages.GlasswarePage import GlasswarePage
from PageObjects.KitchenAndDiningPages.KitchenTextilesPage import KitchenTextilesPage
from PageObjects.KitchenAndDiningPages.MugsAndCupsPage import MugsAndCupsPage as MugsAndCupsPage2
from PageObjects.KitchenAndDiningPages.ServingPiecesPage import ServingPiecesPage
from PageObjects.KitchenAndDiningPages.StorageAndAccessoriesPage import StorageAndAccessoriesPage
from PageObjects.KitchenAndDiningPages.CookingAndRoastingPage import CookingAndRoastingPage as CookingAndRoastingPage2
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
    result = page.has_opened("TEST PREFIX Homepage TEST PREFIX")
    assert result, "'Home' page didn't open!"


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

    @allure.step("Opening 'Sale Room' page from 'Home' page with main menu")
    def test_guest_open_sale_room_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Sale Room' page from 'Home' page with main menu"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_visible_items("Sale Room")
        page = SaleRoomPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Sale Room TEST PREFIX")
        assert result, "'Sale Room' page didn't open!"


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
        result = page.has_opened("TEST PREFIX All Portmeirion TEST PREFIX")
        assert result, "'All Portmeirion' page didn't open!"

    @allure.step("Opening 'Mugs And Cups' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_mugs_and_cups_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Mugs And Cups' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Mugs And Cups")
        page = MugsAndCupsPage1(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Mugs & Cups TEST PREFIX")
        assert result, "'Mugs And Cups' page didn't open!"

    @allure.step("Opening 'Cooking And Roasting' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_cooking_and_roasting_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Cooking And Roasting' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Cooking And Roasting")
        page = CookingAndRoastingPage1(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Cooking & Roasting TEST PREFIX")
        assert result, "'Cooking And Roasting' page didn't open!"

    @allure.step("Opening 'Amor' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_amor_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Amor' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Amor")
        page = AmorPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Amor TEST PREFIX")
        assert result, "'Amor' page didn't open!"

    @allure.step("Opening 'White Porcelain' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_white_porcelain_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'White Porcelain' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("White Porcelain")
        page = WhitePorcelainPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX White Porcelain TEST PREFIX")
        assert result, "'White Porcelain' page didn't open!"

    @allure.step("Opening 'Seashell' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_seashell_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Seashell' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Seashell")
        page = SeashellPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Seashell TEST PREFIX")
        assert result, "'Seashell' page didn't open!"

    @allure.step("Opening 'Candles' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_candles_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Candles' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Candles")
        page = CandlesPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Candles TEST PREFIX")
        assert result, "'Candles' page didn't open!"

    @allure.step("Opening 'Colour Pop' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_colour_pop_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Colour Pop' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Colour Pop")
        page = ColourPopPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Colour Pop TEST PREFIX")
        assert result, "'Colour Pop' page didn't open!"

    @allure.step("Opening 'Replacement Lids' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_replacement_lids_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Replacement Lids' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Replacement Lids")
        page = ReplacementLidsPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Replacement Lids TEST PREFIX")
        assert result, "'Replacement Lids' page didn't open!"

    @allure.step("Opening 'Coupe' page from 'Home' page with 'Main Menu' 'Portmeirion' drop down items")
    def test_guest_open_coupe_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Coupe' page from 'Home' page with 'Main Menu' 'Portmeirion'
           drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_portmeirion_drop_down_items("Coupe")
        page = CoupePage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Coupe TEST PREFIX")
        assert result, "'Coupe' page didn't open!"


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
        result = page.has_opened("TEST PREFIX All Kitchen & Dining TEST PREFIX")
        assert result, "'All Kitchen And Dining' page didn't open!"

    @allure.step("Opening 'Mugs And Cups' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items")
    def test_guest_open_mugs_and_cups_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Mugs And Cups' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Mugs And Cups")
        page = MugsAndCupsPage2(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Mugs & Cups TEST PREFIX")
        assert result, "'Mugs And Cups' page didn't open!"

    @allure.step("Opening 'Kitchen Textiles' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' "
                 "drop down items")
    def test_guest_open_kitchen_textiles_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Kitchen Textiles' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Kitchen Textiles")
        page = KitchenTextilesPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Kitchen Textiles TEST PREFIX")
        assert result, "'Kitchen Textiles' page didn't open!"

    @allure.step("Opening 'Storage And Accessories' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' "
                 "drop down items")
    def test_guest_open_storage_and_accessories_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Storage And Accessories' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Storage And Accessories")
        page = StorageAndAccessoriesPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Storage & Accessories TEST PREFIX")
        assert result, "'Storage And Accessories' page didn't open!"

    @allure.step("Opening 'Cooking And Roasting' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' "
                 "drop down items")
    def test_guest_open_cooking_and_roasting_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Cooking And Roasting' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Cooking And Roasting")
        page = CookingAndRoastingPage2(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Cooking & Roasting TEST PREFIX")
        assert result, "'Cooking And Roasting' page didn't open!"

    @allure.step("Opening 'Cutlery' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items")
    def test_guest_open_cutlery_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Cutlery' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Cutlery")
        page = CutleryPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Cutlery TEST PREFIX")
        assert result, "'Cutlery' page didn't open!"

    @allure.step("Opening 'Glassware' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items")
    def test_guest_open_glassware_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Glassware' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Glassware")
        page = GlasswarePage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Glassware TEST PREFIX")
        assert result, "'Glassware' page didn't open!"

    @allure.step("Opening 'Serving Pieces' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items")
    def test_guest_open_serving_pieces_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Serving Pieces' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Serving Pieces")
        page = ServingPiecesPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Serving Pieces TEST PREFIX")
        assert result, "'Serving Pieces' page didn't open!"

    @allure.step("Opening 'Tableware' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' drop down items")
    def test_guest_open_tableware_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Tableware' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Tableware")
        page = TablewarePage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Tableware TEST PREFIX")
        assert result, "'Tableware' page didn't open!"

    @allure.step("Opening 'Candles And Lighting' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' "
                 "drop down items")
    def test_guest_open_candles_and_lighting_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Candles And Lighting' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Candles And Lighting")
        page = CandlesAndLightingPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Candles & Lighting TEST PREFIX")
        assert result, "'Candles And Lighting' page didn't open!"

    @allure.step("Opening 'Table Linen And Accessories' page from 'Home' page with 'Main Menu' 'Kitchen And Dining' "
                 "drop down items")
    def test_guest_open_table_linen_and_accessories_page_from_home_page_with_main_menu(self, driver, link: str) -> None:
        """Test method. Guest can open 'Table Linen And Accessories' page from 'Home' page with 'Main Menu'
           'Kitchen And Dining' drop down items"""
        page = HomePage(driver, link)
        page.open()
        page.mainMenu.click_to_main_menu_kitchen_and_dining_drop_down_items("Table Linen And Accessories")
        page = CandlesAndLightingPage(driver, driver.current_url)
        result = page.has_opened("TEST PREFIX Table Linen & Accessories TEST PREFIX")
        assert result, "'Table Linen And Accessories' page didn't open!"
