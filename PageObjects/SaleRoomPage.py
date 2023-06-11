from PageObjects.BasePage import BasePage


class SaleRoomPage(BasePage):
    """Class for 'Sale Room' page"""

    def __init__(self, *args, **kwargs) -> None:
        """Constructor for SaleRoomPage class"""
        super(SaleRoomPage, self).__init__(*args, **kwargs)