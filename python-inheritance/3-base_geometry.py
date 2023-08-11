""" 
creating an empty class
 """

class BaseGeometry:
    """
    An empty class representing base geometry.
    """
    @classmethod
    def __dir__(cls):
        # Get all the attributes, including __init_subclass__
        attributes = dir(super())

        # Make a new list without __init_subclass__
        new_attributes = [attr for attr in attributes if attr != '__init_subclass__']

        # Return the new list
        return new_attributes
