class AttributeMismatch(Exception):
    """
    Exception raised when the attributes on the dictionary do not match the attributes on the
    pydantic object
    """

    def __init__(self, message="Attributes on the dictionary do not match the attributes on the object"):
        self.message = message
        super().__init__(self.message)
