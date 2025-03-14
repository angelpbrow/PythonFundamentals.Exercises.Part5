def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    rstr = value[::-1]
    if rstr == value:
        return True
    else: return False

