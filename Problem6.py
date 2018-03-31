from enum import Enum
import scipy.stats as stat
import numpy as np
import scr.InOutFunctions as InOutSupport
import scr.StatisticalClasses as StatSupport
import scr.FormatFunctions as FormatSupport
import Problem4and5 as Cls
import Problem4Settings as CalibSets

##Because we have the same percentage and double the sample size,
# we expect to see a much smaller standard error and therefore a much tighter interval for both.
# The point estimates (mortality probability and mean survival time) should be the same.

# create a calibration object
calibration = Cls.Calibration()

# sample the posterior of the mortality probability
calibration.sample_posterior()

# Estimate of mortality probability and the posterior interval
print('Estimate of mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))

# initialize a calibrated model
calibrated_model = Cls.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model.simulate(CalibSets.NUM_SIM_COHORTS, CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)


# report mean and projection interval
print('Mean survival and {:.{prec}%} interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(CalibSets.ALPHA, deci=4))
