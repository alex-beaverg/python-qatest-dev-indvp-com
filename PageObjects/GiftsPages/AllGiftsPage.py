from PageObjects.BasePage import BasePage


class AllGiftsPage(BasePage):
    """Class for 'All Gifts' page"""

    def __init__(self, *args, **kwargs) -> None:
        """Constructor for AllGiftsPage class"""
        super(AllGiftsPage, self).__init__(*args, **kwargs)