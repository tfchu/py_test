'''
Class hierarchy (standard way)
Exception   -->    Error    --> ValueTooSmallError
                            --> ValueTooLargeError
'''

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    def __init__(self, value):
        self.value = value
        self.message = 'Your value is too small.'
    
    def __str__(self):
        return '{} (Input: {})'.format(self.message, self.value)


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    def __init__(self, value):
        self.value = value
        self.message = 'Your value is too large.'
    
    def __str__(self):
        return '{} (Input: {})'.format(self.message, self.value)