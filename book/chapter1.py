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
with pm.Model() as attackerModel:
    lambda_1 = pm.Exponential("lambda_1", alpha)
    lambda_2 = pm.Exponential("lambda_2", alpha)
    tau = pm.DiscreteUniform("tau", lower=0, upper=n_count_data)
    print("Random output: ", tau.random(), tau.random(), tau.random())
    idx = np.arange(n_count_data)  # Index
    lambda_ = pm.math.switch(tau > idx, lambda_1, lambda_2)#deterministic variable

    # @pm.Deterministic('lambda_', lambda_1, attackerModel)
    #module 'pymc3' has no attribute 'deterministic'; check the online book, take simpler distributions from Scala than Normal distribution for building the prior attacker model
    # def lambda_(tau=tau, lambda_1=lambda_1, lambda_2=lambda_2):
    #     out=np.zeros(n_count_data)
    #     out[:tau]=lambda_1
    #     out[tau:]=lambda_2
    #     return tau
    # lambda_= pm.Deterministic("lambda_", lambda_1, lambda_2)#not working

    observation = pm.Poisson("obs", lambda_, observed=count_data)
    step = pm.Metropolis()
    trace = pm.sample(10000, tune=5000, step=step)
    lambda_1_samples = trace['lambda_1']
    lambda_2_samples = trace['lambda_2']
    tau_samples = trace['tau']
    figsize(12.5, 10)
    # histogram of the samples:

    ax = plt.subplot(311)
    ax.set_autoscaley_on(False)

    plt.hist(lambda_1_samples, histtype='stepfilled', bins=30, alpha=0.85,
             label="posterior of $\lambda_1$", color="#A60628", density=True)
    plt.legend(loc="upper left")
    plt.title(r"""Posterior distributions of the variables
        $\lambda_1,\;\lambda_2,\;\tau$""")
    plt.xlim([15, 30])
    plt.xlabel("$\lambda_1$ value")

    ax = plt.subplot(312)
    ax.set_autoscaley_on(False)
    plt.hist(lambda_2_samples, histtype='stepfilled', bins=30, alpha=0.85,
             label="posterior of $\lambda_2$", color="#7A68A6", density=True)
    plt.legend(loc="upper left")
    plt.xlim([15, 30])
    plt.xlabel("$\lambda_2$ value")

    plt.subplot(313)
    w = 1.0 / tau_samples.shape[0] * np.ones_like(tau_samples)
    plt.hist(tau_samples, bins=n_count_data, alpha=1,
             label=r"posterior of $\tau$",
             color="#467821", weights=w, rwidth=2.)
    plt.xticks(np.arange(n_count_data))

    plt.legend(loc="upper left")
    plt.ylim([0, .75])
    plt.xlim([35, len(count_data) - 20])
    plt.xlabel(r"$\tau$ (in days)")
    plt.ylabel("probability")
    plt.show()
    # model = pm.Model([observation, lambda_1, lambda_2, tau])
    # mcmc = pm.MCMC(model)
    # mcmc.sample(40000, 10000)
    # lambda_1=mcmc.sample()
    # print("lambda_1", lambda_1)
