import pytest

from PageObjects.HomePage import HomePage


@pytest.mark.guest_tests
def test_guest_should_see_home_page(driver):
    link = "https://qatest-dev.indvp.com/"
    page = HomePage(driver, link)
    page.open()
    result = page.has_opened("TEST PREFIX Homepage TEST PREFIX")
    assert result, "[ASSERT MESSAGE]: HomePage didn't open"