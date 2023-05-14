import functools


def pipe(*functions):
    """
    Returns a function that applies all functions in the given order to its
    """
    return functools.reduce(
        lambda f, g: lambda x: f(g(x)) if g else f(x),
        functions[::-1],
        lambda x: x) if functions else None
