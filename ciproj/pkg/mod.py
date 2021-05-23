"""

module doc
"""


class Calculator:
    """
    class doc
    """

    def __init__(self, num1, num2):
        """constructor

        :param num1:
        :param num2:
        """
        self.num1 = num1
        self.num2 = num2

    # pylint: disable=R0201
    def add(self, num1: int, num2: int):
        """ add func

        :param num1:
        :param num2:
        :return:
        """
        return num1 + num2

    def sub(self, num1, num2):
        """sunum2 func

        :param num1:
        :param num2:
        :return:
        """
        return num1 - num2
