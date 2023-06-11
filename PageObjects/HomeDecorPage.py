from PageObjects.BasePage import BasePage


class HomeDecorPage(BasePage):
    """Class for 'Home Decor' page"""

    def __init__(self, *args, **kwargs) -> None:
        """Constructor for HomeDecorPage class"""
        super(HomeDecorPage, self).__init__(*args, **kwargs)
