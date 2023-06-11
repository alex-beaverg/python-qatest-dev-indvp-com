from PageObjects.BasePage import BasePage


class NewInPage(BasePage):
    """Class for 'New In' page"""

    def __init__(self, *args, **kwargs) -> None:
        """Constructor for NewInPage class"""
        super(NewInPage, self).__init__(*args, **kwargs)
