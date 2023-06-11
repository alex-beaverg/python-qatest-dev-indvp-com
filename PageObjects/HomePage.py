from PageObjects.BasePage import BasePage


class HomePage(BasePage):
    """Class for 'Home' page"""
    def __init__(self, *args, **kwargs) -> None:
        """Constructor for HomePage class"""
        super(HomePage, self).__init__(*args, **kwargs)
