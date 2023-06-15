from PageObjects.BasePage import BasePage


class GiftsUnder50Page(BasePage):
    """Class for 'Gifts Under 50' page"""

    def __init__(self, *args, **kwargs) -> None:
        """Constructor for GiftsUnder50Page class"""
        super(GiftsUnder50Page, self).__init__(*args, **kwargs)