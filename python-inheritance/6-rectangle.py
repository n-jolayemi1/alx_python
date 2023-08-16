""" creating a class
 """

class BaseGeometryMeta(type):
    
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
    
class BaseGeometry(metaclass=BaseGeometryMeta):
    """ 
    declaring a attribute that will remove the init subclass
      """

    def __dir__(self):
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

        if isinstance(value, int) or value <= 0:
            raise TypeError("{} must be a positive integer".format(name))
   
        

class Rectangle(BaseGeometry):

    """
    Represents a rectangle with width and height.
    """

    def __init__(self, width=0, height=0):
        """ 
        Inherit a Rectangle from the Basegeometry class

        args: width (int): The width of the rectangle.
                height (int): The height of the rectangle.

            Raises:
                ValueError: If width or height are not positive integers.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
        

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))