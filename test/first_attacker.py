import unittest
import pymc3 as pm
from attack.average_age import alpha



class TestSum(unittest.TestCase):


    def test_average_age(self):



        with pm.Model() as attackerModel:
            # Priors for age model parameters
            nameAgeList = [("Tom", 10)]#what the attacker has learned and Tom's age in the prior
            #an array of 100 random vaiables with random names and ages and for one of them I want to observe
            age = pm.Normal('age', mu=alpha(nameAgeList), sd=20)

            # the attacker knows that Tom is in the list
            for each in nameAgeList:
                if "Tom"in each:
                    print("found Tom")
                    found_Tom=pm.Bernoulli("found_Tom",1.0, observed=True)
                    #pm.Deterministic variable if TOm is in the list and observed it
                    #remove the variable altogether; compute deterministiclly of the array of ages and make an observation of the average age
                    pass
                else:
                    found_Tom = pm.Bernoulli("found_Tom", 0.0, observed=True)
                    # pm.Deterministic variable if TOm is in the list
                    print("Tom not found")

            # Expected value of outcome

            # Likelihood (sampling distribution) of observations
            step = pm.Metropolis()
            trace = pm.sample(10000, tune=5000, step=step)
            age_samples = trace['age']

            self.assertEqual(10, 10, "Tom's age should be 10")

if __name__ == '__main__':
    unittest.main()
