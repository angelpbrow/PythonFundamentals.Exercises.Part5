
from typing import List, Optional, Any
from math import ceil


def get_item_at_position(list_in: List, pos: int) -> List:
    """
    Returns the item at pos.

    :param list_in: Input list
    :param pos: Position of desired item in list_in
    :return: Item in pos
    """
    for i in range(len(list_in)):
        return list_in[pos]


def print_list_items(list_in: List) -> None:
    """
    Given a list, this function iterates through it and prints each element.

    :param list_in: Input list
    :return: None
    """

    for word in list_in:
        print(word)



def sort_by_commit_count(list_in: List) -> List:
    """
    Given a list of entries, return a new list sorted based on the commit count.

    :param list_in: A list where each entry is a list containing a name and the commit count corresponding to a user
    :return: The same list sorted in ascending order based on the commit count
    """
    list_in.sort(key=lambda x: x[1])
    return list_in




def gen_list_of_nums(n: int) -> List[int]:
    """
    Given a number (N), this function returns a list of integers from 0 to N (exclusive).

    :param n: The number of items the result should contain
    :return: A list of integers
    """
    return list(range(n))

def half_list(list_in: List, half: int) -> List:
    """
    Given a list, this function will return a new list that contains half of the items in the list_in parameter.

    :param list_in: The list which will be used to generate the return value
    :param half: 1 will use the first half of the input list. 2 will use the second half of the input list.
    If the length of list_in is an odd number, round the half value up (hint: math.ceil()).
    :return: A list.
    """

    if len(list_in) % 2 == 0:
        if half == 1:
            list_in2 = list_in[:int (len(list_in)/2)]
        elif half == 2:
            list_in2 = list_in[int (len(list_in)/2):]

    if len(list_in) % 2 != 0:
        if half == 1:
            list_in2 = list_in[: ceil(len(list_in)/2)]
        elif half == 2:
            list_in2 = list_in[ceil((-1 * (len(list_in) + 1)) / 2):]

    return list_in2

def remove_odds(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the odd numbers from the same list.

    :return: None
    """

    for i in range(len(list_in)):
        if i % 2 != 0:
            list_in.remove(i)
    return (list_in)

def remove_evens(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the even numbers from the same list.

    :return: None
    """
    for i in range(len(list_in)):
        if i % 2 == 0:
            list_in.remove(i)
    return (list_in)




def concatenate_lists(list_a: List, list_b: List) -> List:
    """
    Given two lists, this function combines them and returns the result as a new list.

    :param list_a: A list
    :param list_b: Another list
    :return: A list containing all elements from list_a and list_b
    """
    list_c = list_a + list_b
    return list_c


def multiply_list(list_in: List, scalar: int) -> Optional[Any]:
    """
    Given a list and an integer, this function will return a new list which is the result of multiplying
    the input list by the value of the scalar.

    :param list_in: A list
    :param scalar: An integer
    :return: A list
    """

    return list_in * scalar
