""" 
creating a a function that check the the instance  of an object
 """
def inherits_from(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
