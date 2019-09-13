# standard libraries 
import sys, os

# non-standard libraries
import pytest

# project libraries
from src.naive_bayes.classifier import tokenize

# sys.path.insert(1, '/Users/dustin/CS/projects/courses/data_science_from_scratch/')



class TestNaiveBayes():


    def test_tokenize(self):
        """Tests the tokenize method
        """

        assert tokenize("Data Science is science") == {"data", "science", "is"}
