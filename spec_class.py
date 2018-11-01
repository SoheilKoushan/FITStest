#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 12:16:05 2018

@author: attila
"""

from astropy.io import fits

class Spectrum(object):
    def __init__(self, file=None): 
        if file is None:
            print("file does not exist")
        self.filepath = file
        self._ra = None
        self._dec = None
        self._read_basics = False
        #hdu_list = fits.open(file)
        #num_hdus = len(hdu_list)
        #self.num_hdus = num_hdus
        #print("This file has {} HDUs.".format(num_hdus))
        #self._ra = None
        #hdu_list.close()

    @property
    def ra(self):
        ''' Returns the RA of this spectrum in degrees. '''
        if self._ra == None:
            #hdu = fits.open(self.filepath)
            #self._ra = hdu[0].header["ra"]
            #hdu.close()
            self.read_basics
        return self._ra

    @property
    def dec(self):
        ''' Returns the RA of this spectrum in degrees. '''
        if self._dec == None:
            #hdu = fits.open(self.filepath)
            #self._dec = hdu[0].header["dec"]
            #hdu.close()
            self.read_basics
        return self._dec

    @property
    def read_basics(self):
        hdu = fits.open(self.filepath)
        self._ra = hdu[0].header["ra"]
        self._dec = hdu[0].header["dec"]
        hdu.close()
        self._read_basics = True
        return self._read_basics
            