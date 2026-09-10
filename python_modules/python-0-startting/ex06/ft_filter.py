def ft_filter(function, iterable):
    """
    Clone of the built-in filter().

    Yields items from iterable for which function(item) is truthy.
    If function is None, yields items that are truthy themselves.
    """
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item
