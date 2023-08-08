""" 
defining a class to get the area of square
 """

class Square:
    """
    Represents a square with a private size attribute.
    """

    def __init__(self, size=0):

        """
        Initializes a Square instance with the provided size.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        return self.__size * self.__size
