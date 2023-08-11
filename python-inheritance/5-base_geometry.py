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
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")