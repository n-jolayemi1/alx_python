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
    def __dir__(self):
        attributes = super().__dir__()
        new_attributes = [attr for attr in attributes if attr != '__init_subclass__']
        return new_attributes

