from typing import List


def flatten_dictionary(d: dict):
    """
    Given a possibly-nested dictionary, return a dot-flattened dictionary.

    Otherwise, return None.

    >>> given_dictionary = {'key': 3, 'foo': {'a': 5, 'bar': {'baz': 8}}}
    >>>
    >>> returned_dictionary = flatten_dictionary(given_dictionary)
    >>> returned_dictionary == {'foo.a': 5, 'foo.bar.baz': 8, 'key': 3}
    True

    :param d: A dictionary
    :return: d, but flattened to a single level of keys
    """
    if type(d) is dict:
        # Use an ordered list of strings to keep track of the current dot-level
        #
        # At this moment, instantiate a single dictionary object to use as
        # our global accumulator.
        #
        # Begin by passing the dictionary we received.
        return descend(namespace=[], accumulator={}, value=d)
    # Otherwise, return None


def descend(namespace: List[str], accumulator: dict, value):
    # Handle this value being a dictionary
    if type(value) is dict:
        # Recurse for each key-value pair in this dictionary
        for key, _value in value.items():
            # Extend this recursion's namespace by this recursion's key
            descend([*namespace, key], accumulator, _value)
    # Handle this value not being a dictionary (i.e. a leaf)
    else:
        accumulator['.'.join(namespace)] = value

    # Return the global accumulator, which should be the flattened dictionary
    return accumulator
