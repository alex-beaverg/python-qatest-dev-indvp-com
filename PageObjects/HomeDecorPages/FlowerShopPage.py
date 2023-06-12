from PageObjects.BasePage import BasePage


class FlowerShopPage(BasePage):
    """Class for 'Flower Shop' page"""

    def __init__(self, *args, **kwargs) -> None:
        """Constructor for FlowerShopPage class"""
        super(FlowerShopPage, self).__init__(*args, **kwargs)