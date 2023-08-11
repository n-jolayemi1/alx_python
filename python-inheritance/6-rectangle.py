""" creating a class
 """

class BaseGeometry:
    """ 
    creating a public instance method that will raise an exception message
      """
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name="", value=0):

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

""" 
creating a class rectangle that inherits from BaseGeometry

return: width and height 
"""
class Rectangle(BaseGeometry):
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
    defininig an initial instance inside rectangle
    """
    def __init__(self, width=None, height=None):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height