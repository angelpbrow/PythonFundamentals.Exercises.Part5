def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    # turn value into all lowercase
    small_str = value.lower()
    #turn lower into strings without spaces
    str_nspace = small_str.replace(" ","")
    # reverse the string without spaces
    rvrs = str_nspace[::-1]
    #compare reversed string without spaces with string without spaces
    return rvrs == str_nspace



