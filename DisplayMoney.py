import pygwidgets  # Assuming pygwidgets is a valid GUI library

BLACK = (0, 0, 0)


class DisplayMoney(pygwidgets.DisplayText):
    """
    A class for displaying monetary values in a GUI application.

    Inherits from `pygwidgets.DisplayText` (assuming it's a base class for text display).

    Attributes:
        currencySymbol (str): The currency symbol to use (default '$').
        currencySymbolOnLeft (bool): Whether to display the currency symbol before
                                    or after the value (default True).
        showCents (bool): Whether to display cents (decimal part) of the value (default True).
    """

    def __init__(self, window, loc, value=None,
                 height=None, fontName=None, fontSize=24, width=150,
                 textColor=BLACK, backgroundColor=None,
                 justified='left', currencySymbol='$',
                 currencySymbolOnLeft=True, showCents=True):
        """
        Initializes a `DisplayMoney` object.

        Args:
            window (object): The window where the object will be displayed.
                (Specific type depends on the pygwidgets library)
            loc (tuple): The location of the object within the window.
                (Specific format depends on pygwidgets)
            value (float, optional): The initial monetary value to display. Defaults to 0.00.
            height (int, optional): The height of the display area. Defaults to None.
            fontName (str, optional): The font name for the displayed text. Defaults to None.
            fontSize (int, optional): The font size for the displayed text. Defaults to 24.
            width (int, optional): The width of the display area. Defaults to 150.
            textColor (tuple, optional): The color of the text. Defaults to BLACK.
            backgroundColor (tuple, optional): The background color of the display area. Defaults to None.
            justified (str, optional): The text justification (left, center, right). Defaults to 'left'.
            currencySymbol (str, optional): The currency symbol to use. Defaults to '$'.
            currencySymbolOnLeft (bool, optional): Whether to display the currency symbol before
                                                    or after the value. Defaults to True.
            showCents (bool, optional): Whether to display cents (decimal part) of the value. Defaults to True.
        """

        self.currencySymbol = currencySymbol
        self.currencySymbolOnLeft = currencySymbolOnLeft
        self.showCents = showCents

        super().__init__(window, loc, value, fontName, fontSize, width, height, textColor, backgroundColor, justified)

    def setValue(self, money):
        """
        Sets the monetary value to display.

        Args:
            money (float or str): The monetary value to display.
        """

        if money == '':
            money = 0.00

        money = float(money)

        if self.showCents:
            formatted_money = '{:,.2f}'.format(money)  # Commas for thousands separators, 2 decimal places
        else:
            formatted_money = '{:,.0f}'.format(money)  # Commas for thousands separators, no decimals

        if self.currencySymbolOnLeft:
            theText = self.currencySymbol + formatted_money
        else:
            theText = formatted_money + self.currencySymbol

        self.currencySymbolOnLeft = currencySymbolOnLeft
        self.showCents = showCents

        super().setValue(theText)
