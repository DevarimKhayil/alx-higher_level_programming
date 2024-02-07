def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
    - my_obj: The object to be serialized.

    Returns:
    A JSON-formatted string.
    """
    import json
    return json.dumps(my_obj)
