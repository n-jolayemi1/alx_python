""" 
creating BaseGeometryMeta class that will remove the __init_subclass from the directory
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
    
""" 
creating a class that inherits from BaseGeometryMeta class that will remove the __init_subclass from the directory
 """
    
class BaseGeometry(metaclass=BaseGeometryMeta):
    def __dir__(self):
        attributes = super().__dir__()
        new_attributes = [attr for attr in attributes if attr != '__init_subclass__']
        return new_attributes

