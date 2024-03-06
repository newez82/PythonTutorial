"""
    when import the double_underscores module, it will run the print statement
    from double_underscore.py and it sets the __name__ to double_underscore.

    The second module's name is __main__ since python is running this file directly.
"""

import double_underscores

print(f"second module's name: {__name__}")
