""" 
creating a class
 """

class BaseGeometry:
    
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
    
