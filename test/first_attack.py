import unittest
from pymc3 import Poisson
from attack.alpha import alpha


class TestSum(unittest.TestCase):

    def test_average_age(self):
        #the attacker knows that Tom is in the list
        seen_Tom = Poisson('seen_Tom', mu=rate, value=masked_values, observed=True)
        nameAgeList = [("Tom", 10)]
        self.assertEqual(alpha(nameAgeList), 10, "Tom's age should be 10")


if __name__ == '__main__':
    unittest.main()
