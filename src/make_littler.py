#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Created by wuxinwang
#
import numpy as np

class header_record():
    """
    This class is use to generate the header record for littler format data
    """
    def __init__(
            self,
            lat: float = 39.78000,
            lon: float = -104.86000,
            id: str = '  station info'.ljust(40,' '),
            name: str = '  surface data from ascat'.ljust(40, ' '),
            fm_code: str = 'FM-281 Quikscat'.ljust(40,' '),
            source: str = 'write_by_wuxin'.ljust(40, ' '),
            elevation: float = format(10, '20.5f'),
            valid_fields: int = format(6*1, '10'),
            num_errors: int = format(0, '10'),
            num_warnings: int = format(0, '10'),
            sequence_number: int = format(0, '10'),
            num_duplicates: int = format(0, '10'),
            is_sound: bool = False,
            is_bogus: bool = False,
            discard: bool = False,
            unix_time: int = format(-888888, '10'),
            julian_day: int = format(-888888, '10'),
            date: int = 202008191208,
            slp: float = format(-888888, '13.5f'),
            slp_qc: int = format(0, '7'),
            ref_pressure: float = format(-888888, '13.5f'),
            ref_perssure_qc: int = format(0, '7'),
            ground_temp: float = format(-888888, '13.5f'),
            ground_temp_qc: int = format(0, '7'),
            sst: float = format(-888888, '13.5f'),
            sst_qc: int = format(0, '7'),
            precip: float = format(-888888, '13.5f'),
            precip_qc: int = format(0, '7'),
            daily_max_t: float = format(-888888, '13.5f'),
            daily_max_t_qc: int = format(0, '7'),
            daily_min_t: float = format(-888888, '13.5f'),
            daily_min_t_qc: int = format(0, '7'),
            night_min_t: float = format(-888888, '13.5f'),
            night_min_t_qc: int = format(0, '7'),
            hr3_pres_change: float = format(-888888, '13.5f'),
            hr3_pres_change_qc: int = format(0, '7'),
            hr24_pres_change: float = format(-888888, '13.5f'),
            hr24_pres_change_qc: int = format(0, '7'),
            cloud_cover: float = format(-888888, '13.5f'),
            cloud_cover_qc: int = format(0, '7'),
            ceiling: float = format(-888888, '13.5f'),
            ceiling_qc: int = format(0, '7'),
            precipitable_water: float = format(-888888, '13.5f'),
            precipitable_water_qc: int = format(0, '7'),
    ):
        if len('{:20.5f}'.format(lat)) > 20:
            lat = np.float('{:20.5f}'.format(lat)[:14])
        self.lat = '{:20.5f}'.format(lat)
        if len('{:20.5f}'.format(lon)) > 20:
            lon = np.float('{:20.5f}'.format(lat)[:14])
        self.lon = format(lon, '20.5f')
        self.id = id
        self.name = name
        self.fm_code = fm_code
        self.source = source
        self.elevation = elevation
        self.valid_fields = valid_fields
        self.num_errors = num_errors
        self.num_warnings = num_warnings
        self.sequence_number = sequence_number
        self.num_duplicates = num_duplicates
        self.is_sound = '     T'.ljust(10, ' ') if is_sound else '     F'.ljust(10, ' ')
        self.is_bogus = '     T'.ljust(10, ' ') if is_bogus else '     F'.ljust(10, ' ')
        self.discard = '     T'.ljust(10, ' ') if discard else '     F'.ljust(10, ' ')
        self.unix_time = unix_time
        self.julian_day = julian_day
        self.date = str(('      '+str(date)).ljust(20, '0'))
        self.slp = slp
        self.slp_qc = slp_qc
        self.ref_pressure = ref_pressure
        self.ref_perssure_qc = ref_perssure_qc
        self.ground_temp = ground_temp
        self.ground_temp_qc = ground_temp_qc
        self.sst = sst
        self.sst_qc = sst_qc
        self.precip = precip
        self.precip_qc = precip_qc
        self.daily_max_t = daily_max_t
        self.daily_max_t_qc = daily_max_t_qc
        self.daily_min_t = daily_min_t
        self.daily_min_t_qc = daily_min_t_qc
        self.night_min_t = night_min_t
        self.night_min_t_qc = night_min_t_qc
        self.hr3_pres_change = hr3_pres_change
        self.hr3_pres_change_qc = hr3_pres_change_qc
        self.hr24_pres_change = hr24_pres_change
        self.hr24_pres_change_qc = hr24_pres_change_qc
        self.cloud_cover = cloud_cover
        self.cloud_cover_qc = cloud_cover_qc
        self.ceiling = ceiling
        self.ceiling_qc = ceiling_qc
        self.precipitable_water = precipitable_water
        self.precipitable_water_qc = precipitable_water_qc

    def make_line(self):
        """
        This function makes one line for header record
        :return: str
        """
        res = self.lat + self.lon + self.id +\
            self.name + self.fm_code + self.source + \
            self.elevation + self.valid_fields + self.num_errors + \
            self.num_warnings + self.sequence_number + self.num_duplicates + \
            self.is_sound + self.is_bogus + self.discard + self.unix_time + \
            self.julian_day + self.date + self.slp + self.slp_qc + \
            self.ref_pressure + self.ref_perssure_qc + self.ground_temp + \
            self.ground_temp_qc + self.sst + self.sst_qc + self.precip + \
            self.precip_qc + self.daily_max_t + self.daily_max_t_qc + \
            self.daily_min_t + self.daily_min_t_qc + self.night_min_t + \
            self.night_min_t_qc + self.hr3_pres_change + self.hr3_pres_change_qc + \
            self.hr24_pres_change + self.hr24_pres_change_qc + self.cloud_cover + \
            self.cloud_cover_qc + self.ceiling + self.ceiling_qc + \
            self.precipitable_water + self.precipitable_water_qc
        return res

    def write(self, file):
        """
        This function is used to write header record to the littler file.
        :param file: The output file which used for WRFDA obsproc module
        :return: None
        """
        file.write(self.make_line())

class data_record():
    """
    This class is use to generate the data record for littler format data
    """
    def __init__(
            self,
            pressure: float = format(-888888, '13.5f'),
            pressure_qc: int = format(0, '7'),
            height: float = format(10, '13.5f'),
            height_qc: int = format(0, '7'),
            temperature: float = format(-888888, '13.5f'),
            temperature_qc: int = format(0, '7'),
            dew_point: float = format(-888888, '13.5f'),
            dew_point_qc: int = format(0, '7'),
            wind_speed: float = 20,
            wind_speed_qc: int = format(0, '7'),
            wind_dir: float = 180,
            wind_dir_qc: int = format(0, '7'),
            wind_u: float = format(-888888, '13.5f'),
            wind_u_qc: int = format(0, '7'),
            wind_v: float = format(-888888, '13.5f'),
            wind_v_qc: int = format(0, '7'),
            relative_humidity: float = format(-888888, '13.5f'),
            relative_humidity_qc: int = format(0, '7'),
            thickness: float = format(-888888, '13.5f'),
            thickness_qc: int = format(0, '7'),
    ):
        self.pressure = pressure
        self.pressure_qc = pressure_qc
        self.height = height
        self.height_qc = height_qc
        self.temperature = temperature
        self.temperature_qc = temperature_qc
        self.dew_point = dew_point
        self.dew_point_qc = dew_point_qc
        self.wind_speed = format(wind_speed, '13.5f')
        self.wind_speed_qc = wind_speed_qc
        self.wind_dir = format(wind_dir, '13.5f')
        self.wind_dir_qc = wind_dir_qc
        self.wind_u = wind_u
        self.wind_u_qc = wind_u_qc
        self.wind_v = wind_v
        self.wind_v_qc = wind_v_qc
        self.relative_humidity = relative_humidity
        self.relative_humidity_qc = relative_humidity_qc
        self.thickness = thickness
        self.thickness_qc = thickness_qc

    def make_line(self):
        """
        This function makes one line of the data record
        :return: str
        """
        res = self.pressure + self.pressure_qc + self.height + \
              self.height_qc + self.temperature + self.temperature_qc + \
              self.dew_point + self.dew_point_qc + self.wind_speed + \
              self.wind_speed_qc + self.wind_dir + self.wind_dir_qc + \
              self.wind_u + self.wind_u_qc + self.wind_v + \
              self.wind_v_qc + self.relative_humidity + self.relative_humidity_qc + \
              self.thickness + self.thickness_qc
        return res

    def write(self, file):
        """
            This function is used to write data record to the littler file.
            :param file: The output file which used for WRFDA obsproc module
            :return: None
        """
        file.write(self.make_line())

class ending_record():
    """
        This class is use to generate the ending record for littler format data
    """
    def __init__(self):
        self.ending_1 = format(-777777., '13.5f')
        self.ending_2 = format(0, '7')
        self.ending_3 = format(-777777., '13.5f')
        self.ending_4 = format(0, '7')
        self.ending_5 = format(1, '13.5f')
        self.ending_6 = format(0, '7')
        self.ending_7 = format(-888888., '13.5f')
        self.ending_8 = format(0, '7')
        self.ending_9 = format(20., '13.5f')
        self.ending_10 = format(0, '7')
        self.ending_11 = format(180, '13.5f')
        self.ending_12 = format(0, '7')
        self.ending_13 = format(-888888., '13.5f')
        self.ending_14 = format(0, '7')
        self.ending_15 = format(-888888., '13.5f')
        self.ending_16 = format(0, '7')
        self.ending_17 = format(-888888., '13.5f')
        self.ending_18 = format(0, '7')
        self.ending_19 = format(-888888., '13.5f')
        self.ending_20 = format(0, '7')

    def make_line(self):
        """
        This function make one line of the ending record
        :return: str
        """
        res = self.ending_1 + self.ending_2 + self.ending_3 + self.ending_4 + \
              self.ending_5 + self.ending_6 + self.ending_7 + self.ending_8 + \
              self.ending_9 + self.ending_10 + self.ending_11 + self.ending_12 + \
              self.ending_13 + self.ending_14 + self.ending_15 + self.ending_16 + \
              self.ending_17 + self.ending_18 + self.ending_19 + self.ending_20
        return res

    def write(self, file):
        """
            This function is used to write ending record to the littler file.
            :param file: The output file which used for WRFDA obsproc module
            :return: None
        """
        file.write(self.make_line())