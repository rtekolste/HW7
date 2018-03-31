##What is the probability that 64.9% of patients survive when 50% are expected?
##What is the probability that 400 survive 286.5 are expected?
##Assume that 50% is the real (null) hypothesis.

from scipy.stats import binom
print(binom.pmf(k=400, n=573, p=0.5))

