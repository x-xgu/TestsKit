def patch_method_in(cls):
    """
    Decorator to patch method in class
    """
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


def patch_class(name, bases, namespace):
    """
    Patch class with given name, bases and namespace
    """
    assert len(bases) == 1, "Exactly one base class required"
    base = bases[0]
    for name, value in namespace.iteritems():
        if name != "__metaclass__":
            setattr(base, name, value)
    return base
