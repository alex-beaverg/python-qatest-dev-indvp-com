from PageObjects.BasePage import BasePage


class FurniturePage(BasePage):
    """Class for 'Furniture' page"""

    def __init__(self, *args, **kwargs) -> None:
        """Constructor for FurniturePage class"""
        super(FurniturePage, self).__init__(*args, **kwargs)