""" creating a class
 """

class BaseGeometry:

    """ 
    declaring a attribute that will remove the init subclass
      """

    def __dir__(cls):
        # Get all the attributes, including __init_subclass__
        attributes = super().__dir__()

        # Make a new list without __init_subclass__
        new_attributes = [attr for attr in attributes if attr != '__init_subclass__']

        # Return the new list
        return new_attributes
    
    """ 
    creating a public instance method that will raise an exception message
      """
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name="", value=0):

        if not isinstance(value, int) or value <= 0:
            raise TypeError("{} must be a positive integer".format(name))
        

class Rectangle(BaseGeometry):

    """
    Represents a rectangle with width and height.
    """

    def __init__(self, width, height):
        """ 
        Inherit a Rectangle from the Basegeometry class

        args: width (int): The width of the rectangle.
                height (int): The height of the rectangle.

            Raises:
                ValueError: If width or height are not positive integers.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height