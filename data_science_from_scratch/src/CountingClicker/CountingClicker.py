# I will play around with the concepts outlined in Chapter 2 of Data Science from Scratch by Joel Grus.
# The chatpter covers a basic introduction to Python. The concepts I am most excited to trial are those
#   pertaining to structuring a class and writing methods that involve the self object. 
# I also learned about Type Annotations, which I had not encountered previous. Generally, I am excited
#   to learn the styles of writting good code, and I think Type Annotations will be an important part
#   of writing readable code. 

# As a note, these examples are taken nearly directly from the book, so I acknowledge the book as a source.

class CountingClicker:
    """Simple class that increments and resets a counter """

    def __init__(self, count: int = 0):
        self.count = 0

    def __repr__(self) -> str:
        """Produces the string representation of a class instance"""

        return f"CountingClicker(count={self.count})"

    def click(self, num_times: int = 1):
        """Click the clicker some number of times."""
        self.count += num_times

    def read(self) :
        return self.count
    
    def reset(self):
        self.count = 0 


if __name__ == "__main__":
    
    #a few tests to check that Clicker is doing what I want
    clicker = CountingClicker()
    assert clicker.read() == 0, "clicker should start with count 0"
    clicker.click()
    clicker.click()
    assert clicker.read() == 2, "after two clicks, clicker should have count 2"
    clicker.reset()
    assert clicker.read() == 0, "after reset, the clicker should be back at 0"