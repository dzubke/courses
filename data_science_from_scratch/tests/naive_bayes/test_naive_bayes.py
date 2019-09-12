# standard libraries 
import sys 

# non-standard libraries
import pytest

# project libraries
from naive_bayes.classifier import tokenize

sys.path.insert(1, '/Users/dustin/CS/projects/courses/data_science_from_scratch/src/')

class TestNaiveBayes():


    def test_tokenize(self):
        """Tests the tokenize method
        """

        assert tokenize("Data Science is science") == {"data", "science", "is"}
