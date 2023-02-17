"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        "create serial generator from starting number"
        self.start = start - 1
        self.counter = self.start

    def __repr__(self):
        return f'<SerialGenerator start={self.start + 1} next={self.start + 2}>'

    def generate(self):
        "generate the next sequential number"
        self.counter += 1
        return self.counter

    def reset(self):
        "reset number back to starting number"
        self.counter = self.start
