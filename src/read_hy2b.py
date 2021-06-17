#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Created by wuxinwang
#

import h5py
import numpy as np
import pandas as pd


def read_hy2b(file_path):
    """
	    This function is used to read wind speed and wind direction fom hy2b l2b file
	    in hdf5 format.
	    :param file_path: the path of the hy2b l2b file, which has a endfix '.h5'
	    :return: The data and date which are returned from this function is used to create
	 	    littler format data for WRFDA
	"""
    # ===========================================================================
    # Read HDF5 file.
    f = h5py.File(file_path, "r")  # mode = {'w', 'r', 'a'}

    # Print the keys of groups and datasets under '/'.
    # print(f.filename, ":")
    # print([key for key in f.keys()], "\n")
    lat = np.array(f['wvc_lat'][:]).astype(np.float).flatten()
    for i in range(len(lat)):
        lat[i] = lat[i]

    lon = np.array(f['wvc_lon'][:]).astype(np.float).flatten()
    for i in range(len(lon)):
        lon[i] = lon[i]
    dates = np.array(f['wvc_row_time']).flatten()
    date = dates[len(dates) // 2]
    date = (date[:8] + date[9:11]).decode()
    wind_speed = np.array(f['wind_speed_selection'][:]).astype(np.float).flatten()
    for i in range(len(wind_speed)):
        wind_speed[i] = wind_speed[i] * 0.01

    wind_dir = np.array(f['wind_dir_selection'][:]).astype(np.float).flatten()
    for i in range(len(wind_dir)):
        wind_dir[i] = wind_dir[i] * 0.1

    data = {
        'lat': lat,
        'lon': lon,
        'wind_speed': wind_speed,
        'wind_dir': wind_dir
    }
    df = pd.DataFrame(data)
    # Save and exit the file
    f.close()

    return df, date