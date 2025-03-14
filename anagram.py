def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    #checking if strings are the same length
    if len(first_string) == len (second_string):
        #sort the strings if same length
        str1 = sorted(first_string)
        str2 = sorted(second_string)
        if str1 == str2:
            return True
        elif first_string == second_string: #weed out the words that are the exact word
             return False
        else:
            return False




