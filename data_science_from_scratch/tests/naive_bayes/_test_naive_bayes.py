# standard libraries 
import unittest    
import sys 

# project libraries
from naive_bayes.classifier import tokenize

sys.path.insert(1, '/Users/dustin/CS/projects/courses/data_science_from_scratch/naive_bayes')

class TestNaiveBayes(unittest.TestCase):


    def test_tokenize(self):
        """Tests the tokenize method
        """

        self.assertEqual(tokenize("Data Science is science"), {"data", "science", "is"})
