# -*- coding: utf-8 -*-

#  workadays
#  ----------------------------------------------------------------------
#  Versão simplificada e customizada do pacote holidays
#  ----------------------------------------------------------------------
#       Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#                dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#       Website: https://github.com/dr-prodigy/python-holidays
#       License: MIT (see LICENSE file)
#  ----------------------------------------------------------------------

from workadays.countries import *
from workadays.constants import MON, TUE, WED, THU, FRI, SAT, SUN, WEEKEND
from workadays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from workadays.holiday_base import HolidayBase, createHolidaySum

if not __name__ == '__main__':
    from .main import *
