from errors import InvalidRowLength, NullValueError, InvalidStringLength, InvalidValueError
from typing import List, Any

def is_header(row: List) -> bool:
    """
    Check if a row is a header.

    A row is assumed to be a header if it contains no numeric elements.

    Args:
        row (List): The row to check.

    Returns:
        bool: True if the row is a header, False otherwise.
    """
    for element in row:
        if isinstance(element, (int, float)):
            return False
    return True


def validate_attribute(attribute: str, constraints: dict, value: Any) -> None:
    """
    Validate the value of an attribute based on given constraints.

    Args:
        attribute (str): The name of the attribute being validated.
        constraints (dict): A dictionary containing constraints for the attribute.
            The dictionary should have keys "null" (boolean), "type" (string), and "len" (int).
        value (Any): The value of the attribute being validated.

    Raises:
        NullValueError: If the value is None and the "null" constraint is False.
        InvalidValueError: If the value is not of the expected type based on the "type" constraint.
        InvalidStringLength: If the value exceeds the maximum length specified in the "len" constraint.
    """
    if constraints["null"] is False:
        if value is None:
            raise NullValueError(attribute)
        
    if constraints["type"] == "int":
        try:
            int(value)
        except ValueError:
            raise InvalidValueError(attribute, "int", value)
    
    elif constraints["type"] == "decimal":
        try:
            float(value)
        except ValueError:
            raise InvalidValueError(attribute, "decimal", value)
    
    elif constraints["type"] == "varchar":
        if len(value) > constraints["len"]:
            raise InvalidStringLength(attribute, constraints["len"])


def validate_row(row: List, attributes: dict, number_of_attributes: int) -> bool:
    """
    Validate a row of attributes based on given constraints.

    Args:
        row (List): The row of attribute values to validate.
        attributes (dict): A dictionary mapping attribute names to their corresponding constraints.
            Each constraint dictionary should have keys "null" (boolean), "type" (string), and "len" (int).
        number_of_attributes (int): The expected number of attributes in the row.

    Returns:
        bool: True if the row passes validation, False otherwise.

    Raises:
        InvalidRowLength: If the length of the row is not equal to the expected number of attributes.
        NullValueError: If a non-nullable attribute has a null value.
        InvalidValueError: If an attribute value does not meet its type constraint.
        InvalidStringLength: If an attribute value exceeds its maximum length constraint.
    """

    # Check if row has the right number of fields
    row_len = len(row)
    if row_len != number_of_attributes:
        raise InvalidRowLength(number_of_attributes, row_len)
    
    # Validate each field individually
    index = 0
    for attr in attributes:
        validate_attribute(attr, attributes[attr], row[index])
        index += 1
    
    # Return true only if all the fields are valid
    return True


