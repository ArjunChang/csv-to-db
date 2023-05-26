from typing import Any

class InvalidRowLength(BaseException):
    """
    Custom exception for invalid row length.
    Raised when the expected number of attributes in a row is not equal to the actual number of attributes found.
    """

    def __init__(self, expected_row_length: int, actual_row_length: int):
        """
        Initialize the InvalidRowLength exception.

        Args:
            expected_row_length (int): The expected number of attributes in a row.
            actual_row_length (int): The actual number of attributes found in the row.
        """
        self.message = f"Expected {expected_row_length} attributes. Got {actual_row_length}"
        super().__init__(self.message)


class NullValueError(BaseException):
    """
    Custom exception for null value.
    Raised when a null value is encountered for a specific attribute.
    """

    def __init__(self, attribute: str):
        """
        Initialize the NullValueError exception.

        Args:
            attribute (str): The attribute that cannot be null.
        """
        self.message = f"{attribute} cannot be null."
        super().__init__(self.message)


class InvalidStringLength(BaseException):
    """
    Custom exception for invalid string length.
    Raised when a string attribute exceeds a maximum length.
    """

    def __init__(self, attribute: str, max_length: int):
        """
        Initialize the InvalidStringLength exception.

        Args:
            attribute (str): The attribute with the invalid length.
            max_length (int): The maximum allowed length for the attribute.
        """
        self.message = f"{attribute} cannot exceed maximum length of {max_length}."
        super().__init__(self.message)


class InvalidValueError(BaseException):
    """
    Custom exception for invalid attribute value.
    Raised when an attribute has an invalid value of a different type than expected.
    """

    def __init__(self, attribute: str, expected_type: str, value: Any):
        """
        Initialize the InvalidValueError exception.

        Args:
            attribute (str): The attribute with the invalid value.
            expected_type (type): The expected type for the attribute.
            value (Any): The actual value encountered.
        """
        self.message = f"Expected {expected_type} for {attribute}. Got {value}"
        super().__init__(self.message)
