from PageObjects.BasePage import BasePage


class AccessoriesPage(BasePage):
    """Class for 'Accessories' page"""

    def __init__(self, *args, **kwargs) -> None:
        """Constructor for AccessoriesPage class"""
        super(AccessoriesPage, self).__init__(*args, **kwargs)