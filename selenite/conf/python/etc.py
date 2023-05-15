def list_intersection(one: list, another: list, /):
    """
    Return intersection of two lists
    """
    return list(set(one) & set(another))
