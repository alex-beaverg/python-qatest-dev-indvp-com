from PageObjects.BasePage import BasePage


class ServingPiecesPage(BasePage):
    """Class for 'Serving Pieces' page"""

    def __init__(self, *args, **kwargs) -> None:
        """Constructor for ServingPiecesPage class"""
        super(ServingPiecesPage, self).__init__(*args, **kwargs)