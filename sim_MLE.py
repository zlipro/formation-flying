#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:12:38 2021

@author: zli
"""
import multiprocessing as mp
from framework import Framework
from datetime import datetime
import numpy as np

'''
simulate MLE varying T
'''

MC_RUNS = 50
dt = 0.001
t = 30
ITR = int(t/dt)

### MLE sims
# Noiseless
T=1
start = datetime.now()
def MC_sim(id):
    target = Framework('hexagon', 'opt', T, dt, t,sigma_v=0,sigma_w=0,seed=id)   
    target.run()
    error = target.evaluate()
    return error

pool = mp.Pool(MC_RUNS)
error_noiseless = np.array(pool.map(MC_sim, range(MC_RUNS)))
pool.close()
pool.join()
np.savetxt('results/noiseless.txt',error_noiseless)
print('noiseless took',datetime.now()-start)


# no estimator
T=1
start = datetime.now()
def MC_sim(id):
    target = Framework('hexagon', 'opt', T, dt, t,sigma_v=0.01,sigma_w=0,seed=id)   
    target.run()
    error = target.evaluate()
    return error

pool = mp.Pool(MC_RUNS)
error_no_est = np.array(pool.map(MC_sim, range(MC_RUNS)))
pool.close()
pool.join()
np.savetxt('results/noest.txt',error_no_est)
print('no estimator took',datetime.now()-start)


# T=10 MLE
T=10
start = datetime.now()
def MC_sim(id):
    target = Framework('hexagon', 'opt', T, dt, t,sigma_v=0.01,sigma_w=0,seed=id)   
    target.run()
    error = target.evaluate()
    return error

pool = mp.Pool(MC_RUNS)
error_MLE10 = np.array(pool.map(MC_sim, range(MC_RUNS)))
pool.close()
pool.join()
np.savetxt('results/MLE10.txt',error_MLE10)
print('MLE10 took',datetime.now()-start)


# T=100 MLE
T=100
start = datetime.now()
def MC_sim(id):
    target = Framework('hexagon', 'opt', T, dt, t,sigma_v=0.01,sigma_w=0,seed=id)   
    target.run()
    error = target.evaluate()
    return error

pool = mp.Pool(MC_RUNS)
error_MLE100 = np.array(pool.map(MC_sim, range(MC_RUNS)))
pool.close()
pool.join()
np.savetxt('results/MLE100.txt',error_MLE100)
print('MLE100 took',datetime.now()-start)





