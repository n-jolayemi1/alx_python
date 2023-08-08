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
        
        self.__size = size
    
    """ 
     setting a property for the instance size
    """
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
