#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Created by wuxinwang
#

import h5py
import numpy as np
import pandas as pd
from .utils import uv2sd

def read_windadata(file_path):
    """
	    This function is used to read wind speed and wind direction fom winddata file
	    in hdf format.
	    :param file_path: the path of the winddata, which has a endfix '.hdf'
	    :return: The data and date which are returned from this function is used to create
	 	    littler format data for WRFDA
	"""
    # ===========================================================================
    # Read HDF5 file.
    f = h5py.File(file_path, "r")  # mode = {'w', 'r', 'a'}
    lat = np.array(f['latitude'][:]).astype(np.float).flatten()
    lon = np.array(f['longitude'][:]).astype(np.float).flatten()
    date = str.split(f.filename, '/')[-1][4:-4]
    uwnd = np.array(f['uwnd'][:]).astype(np.float).flatten()
    vwnd = np.array(f['vwnd'][:]).astype(np.float).flatten()
    wspd, wdir = uv2sd(uwnd, vwnd)
    for i in range(len(uwnd)):
        if uwnd[i] == -9999 or vwnd[i] == -9999:
            wspd[i] = -888888.0
            wdir[i] = -888888.0
    data = {
        'lat': lat,
        'lon': lon,
        'wind_speed': wspd,
        'wind_dir': wdir
    }
    df = pd.DataFrame(data)
    # Save and exit the file
    f.close()

    return df, date