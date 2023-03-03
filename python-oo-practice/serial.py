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

    >>> serial
    <SerialGenerator> start=100 next=101
    """
    def __init__(self, start=100):
        self.start = start
        self.count = 0
    
    def __repr__(self):
        return f"<SerialGenerator> start={self.start} next={self.start+self.count}"

    def generate(self):
        """returns the current number and increases the count for the next number"""
        self.count += 1
        return self.start + self.count - 1
    
    def reset(self):
        """sets count to 0"""
        self.count = 0