import pymc3 as pm
from IPython.core.pylabtools import figsize
import numpy as np
import matplotlib.pyplot as plt

figsize(12.5, 3.5)
count_data = np.loadtxt("../data/txtdata.csv")
n_count_data = len(count_data)
plt.bar(np.arange(n_count_data), count_data, color="#348ABD")
plt.xlabel("Time (days)")
plt.ylabel("count of text-msgs received")
plt.title("Did the user's texting habits change over time?")
plt.xlim(0, n_count_data);

alpha = 1.0 / count_data.mean()  # Recall count_data is the  variable that holds our txt counts
#Andrzej idea using mapping and reducing as I did in Figaro for the model
with pm.Model() as auctionModel:
    lambda_1 = pm.Exponential("lambda_1", alpha)
    lambda_2 = pm.Exponential("lambda_2", alpha)
    tau = pm.DiscreteUniform("tau", lower=0, upper=n_count_data)
    print("Random output: ", tau.random(), tau.random(), tau.random())
    @pm.deterministic#module 'pymc3' has no attribute 'deterministic'
    def lambda_(tau=tau, lambda_1=lambda_1, lambda_2=lambda_2):
        out=np.zeros(n_count_data)
        out[:tau]=lambda_1
        out[tau:]=lambda_2
        return tau
    observation = pm.Poisson("obs", lambda_, value=count_data, observed=True)
    model = pm.Model([observation, lambda_1, lambda_2, tau])
    mcmc = pm.MCMC(model)
    mcmc.sample(40000, 10000)
    lambda_1=mcmc.sample()
