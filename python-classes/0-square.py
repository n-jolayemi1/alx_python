""" 
defining a class to get the area of square
 """

class Square:
    """
    Represents a square with a private size attribute.
    """

    def __init__(self, size=None):

        """
        Initializes a Square instance with the provided size.

        Args:
            size (int): The size of the square.
        """

        self.__size = size