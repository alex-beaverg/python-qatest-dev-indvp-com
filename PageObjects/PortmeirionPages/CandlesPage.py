from PageObjects.BasePage import BasePage


class CandlesPage(BasePage):
    """Class for 'Candles' page"""

    def __init__(self, *args, **kwargs) -> None:
        """Constructor for CandlesPage class"""
        super(CandlesPage, self).__init__(*args, **kwargs)