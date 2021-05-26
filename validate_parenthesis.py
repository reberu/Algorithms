def validate(string, d=None):
    """
    :param string: An expression to check.
    :param d: An empty list where we will put parentheses.
    :return: True if parenthesis are balanced or not in expression. False if not balanced.
    """
    if d is None:
        d = []
    for char in string:
        if char in '[({})]':
            d.append(char)
            if len(d) > 1:
                if (d[len(d) - 2] == '[' and d[len(d) - 1] == ']') \
                        or (d[len(d) - 2] == '{' and d[len(d) - 1] == '}') \
                        or (d[len(d) - 2] == '(' and d[len(d) - 1] == ')'):
                    d.pop()
                    d.pop()
    return True if not d else False


print(validate('{}{}())'))  # False
print(validate('(){}[]'))   # True
print(validate(''))         # True
