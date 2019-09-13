# standard python libraries
import math

# non-standard libraries
import pytest

# project libraries
from src.naive_bayes.classifier import tokenize, Message, NaiveBayesClassifier


class TestNaiveBayes():


    def test_tokenize(self):
        """Tests the tokenize method"""

        assert tokenize("Data Science is science") == {"data", "science", "is"}
    
    def test_NaiveBayesClassifier_train(self):
        """ Tests train method in the Naive Bayes Classifier class"""

        messages = [Message("spam rules", is_spam=True),
                    Message("ham rules", is_spam=False),
                    Message("hello ham", is_spam=False)]

        model = NaiveBayesClassifier(k=0.5)
        model.train(messages)

        assert model.tokens == {"spam", "ham", "rules", "hello"}
        assert model.spam_messages == 1
        assert model.ham_messages == 2
        assert model.token_spam_counts == {"spam": 1, "rules": 1}
        assert model.token_ham_counts == {"ham": 2, "rules": 1, "hello": 1}
        
        text = "hello spam"

        probs_if_spam = [
            (1 + 0.5) / (1 + 2 * 0.5),      # "spam"  (present)
            1 - (0 + 0.5) / (1 + 2 * 0.5),  # "ham"   (not present)
            1 - (1 + 0.5) / (1 + 2 * 0.5),  # "rules" (not present)
            (0 + 0.5) / (1 + 2 * 0.5)       # "hello" (present)
        ]

        probs_if_ham = [
            (0 + 0.5) / (2 + 2 * 0.5),      # "spam"  (present)
            1 - (2 + 0.5) / (2 + 2 * 0.5),  # "ham"   (not present)
            1 - (1 + 0.5) / (2 + 2 * 0.5),  # "rules" (not present)
            (1 + 0.5) / (2 + 2 * 0.5),      # "hello" (present)
        ]

        p_if_spam = math.exp(sum(math.log(p) for p in probs_if_spam))
        p_if_ham = math.exp(sum(math.log(p) for p in probs_if_ham))

        # Should be about 0.83
        assert model.predict(text) == p_if_spam / (p_if_spam + p_if_ham)