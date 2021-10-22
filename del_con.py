#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:29:49 2021

@author: wangjinliang
"""
import matplotlib.pyplot as plt
import numpy as np
# import pickle
import laspec.normalization as normalize
from laspec.mrs import MrsFits, MrsSource
mf = MrsFits("/Users/wangjinliang/Downloads/med-58535-HIP25252H332601_sp11-167.fits")
me = mf.get_one_epoch(lmjm=84290179 , norm_type="spline", niter=3)
mer = me.reduce(norm_type="spline", niter=3)
print(mf.info())
print(mf[1].header["SNR"])
print(mf[2].header["SNR"])