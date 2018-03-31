#Calibrate the survival model (with patient cohort size of 1,000)
# using the results of the clinical study described above (i.e. 400 of 573
# participants survived at the end of the 5-year study period).
# Report the estimated annual mortality probability and the 95% credible interval.

SIM_POP_SIZE = 1000       # population size of simulated cohorts
TIME_STEPS = 1000        # length of simulation
ALPHA = 0.05             # significance level for calculating confidence intervals
NUM_SIM_COHORTS = 500   # number of simulated cohorts used to calculate prediction intervals

# details of a clinical study estimating the mean survival time
OBS_N = 573.0        # number of patients involved in the study
OBS_FIVE_YEAR = 400.0
OBS_FIVE_YEAR_RATE = 0.698

# the standard deviation of the mean survival time reported in the clinical study
# assumes that the reported confidence interval in this study is a t-confidence interval
OBS_STDEV = 0.459
      #(((OBS_N-OBS_FIVE_YEAR)/OBS_N)(OBS_FIVE_YEAR/OBS_N))**(1.0/2.0)
      # 0.459 # ((400/573)(173/573))^(1/2)

# how to sample the posterior distribution of mortality probability
# minimum, maximum and the number of samples for the mortality probablity
POST_L, POST_U, POST_N = 0.05, 0.25, 1000
