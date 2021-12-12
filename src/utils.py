#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Created by wuxinwang
#
import numpy as np

MONTH_DAY_0 = {
    'Jan': 31,
    'Feb': 28,
    'Mar': 31,
    'Apr': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'Aug': 31,
    'Sep': 30,
    'Oct': 31,
    'Nov': 30,
    'Dec': 31
}

MONTH_DAY_1 = {
    'Jan': 31,
    'Feb': 29,
    'Mar': 31,
    'Apr': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'Aug': 31,
    'Sep': 30,
    'Oct': 31,
    'Nov': 30,
    'Dec': 31
}

def num2month(month):
    if month == 1:
        return 'Jam'
    elif month == 2:
        return 'Feb'
    elif month == 3:
        return 'Mar'
    elif month == 4:
        return 'Apr'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'Aug'
    elif month == 9:
        return 'Sep'
    elif month == 10:
        return 'Oct'
    elif month == 11:
        return 'Nov'
    elif month == 12:
        return 'Dec'

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return MONTH_DAY_1
    else:
        return MONTH_DAY_0

deg = 180.0/np.pi
rad = np.pi/180.0

def uv2sd(u, v):
    # u, v to wspd, wdir
    wspd = np.sqrt(u**2+v**2)
    wdir =  180.0 + np.arctan2(u, v)*deg
    return wspd, wdir

def sd2uv(wspd, wdir):
    # wspd, wdir to u, v
    u = -wspd*np.sin(wdir*rad)
    v = -wspd*np.cos(wdir*rad)
    print('wspd =',wspd, ' wdir =',wdir, ' u =',u, ' v =',v)