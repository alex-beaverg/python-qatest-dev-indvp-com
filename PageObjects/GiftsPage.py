from PageObjects.BasePage import BasePage


class GiftsPage(BasePage):
    """Class for 'Gifts' page"""

    def __init__(self, *args, **kwargs) -> None:
        """Constructor for GiftsPage class"""
        super(GiftsPage, self).__init__(*args, **kwargs)