#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 12:16:05 2018

@author: attila
"""

from astropy.io import fits

class Spectrum(object):
    def __init__(self, file=None): 
        self.filepath = file
        hdu_list = fits.open(file)
        num_hdus = len(hdu_list)
        self.num_hdus = num_hdus
        print("This file has {} HDUs.".format(num_hdus))
    
        hdu_list.close()

