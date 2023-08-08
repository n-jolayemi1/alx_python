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
    
    """ 
     property setter def size(self, value): to set it:
     size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
     if size is less than 0, raise a ValueError exception with the message size must be >= 0
    """
    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ 
     Public instance method: def area(self): that returns the current square area
    """
    def area(self):
        return self.__size * self.__size
    
    """ 
     Public instance method: def my_print(self): that prints in stdout the square with the character 
     #:if size is equal to 0, print an empty line
    """
    def my_print(self):

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#"*self.__size)
