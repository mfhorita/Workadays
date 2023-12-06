# -*- coding: utf-8 -*-

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, MO, TU

from workadays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, OCT, NOV, DEC, TUE, THU, SAT, SUN
from workadays.holiday_base import HolidayBase


class Argentina(HolidayBase):
    """
    https://pt.wikipedia.org/wiki/Feriados_na_Argentina
    """

    def __init__(self, **kwargs):
        self.country = 'AR'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, JAN, 1)] = "Año Nuevo"
        if self.observed and date(year, JAN, 1).weekday() == SUN:
            self[date(year, JAN, 1) + rd(days=+1)] = "Año Nuevo (Observed)"
        elif self.observed and date(year, JAN, 1).weekday() == SAT:
            self[date(year, JAN, 1) + rd(days=-1)] = "Año Nuevo (Observed)"

        # Carnaval
        quaresma = easter(year) - rd(days=46)  # self[quaresma] = "Quarta-feira de cinzas (Início da Quaresma)"
        self[quaresma - rd(weekday=TU(-1)) - rd(days=1)] = "Carnaval"
        self[quaresma - rd(weekday=TU(-1))] = "Carnaval"

        self[date(year, MAR, 24)] = "Día de la Verdad y la Justicia"

        self[date(year, APR, 2)] = "Día del Veterano de la Guerra das Malvinas"

        # Páscoa
        self[easter(year) - rd(days=3)] = "Jueves Santo"
        self[easter(year) - rd(days=2)] = "Viernes Santo"
        self[easter(year)] = "Páscoa"

        # Dia del Trabajo
        self[date(year, MAY, 1)] = "Día Internacional del Trabajo"

        self[date(year, MAY, 25)] = "Revolución de Mayo"
        if date(year, MAY, 25).weekday() == TUE:
            self[date(year, MAY, 24)] = "Feriado Puente - Revolución de Mayo"
        elif date(year, MAY, 25).weekday() == THU:
            self[date(year, MAY, 26)] = "Feriado Puente - Revolución de Mayo"

        self[date(year, JUN, 17)] = "Muerte del General Martín Miguel de Güemes"

        self[date(year, JUN, 20)] = "Muerte del Gral. Manuel Belgrano - Dia del Bandera"

        self[date(year, JUL, 9)] = "Día de la Independencia"

        # Dia Móvel (Tercera lunes del mês)
        self[date(year, AUG, 1) + rd(weekday=MO(3))] = "Muerte del general José de San Martín"

        self[date(year, OCT, 9)] = "Día de la Raza"

        self[date(year, NOV, 20)] = "Día de la Soberanía Nacional"

        self[date(year, DEC, 8)] = "Inmaculada Concepción de María"

        # Christmas Day
        self[date(year, DEC, 25)] = "Natal"
        if self.observed and date(year, DEC, 1).weekday() == SUN:
            self[date(year, DEC, 25) + rd(days=+1)] = "Natal (Observed)"
        elif self.observed and date(year, DEC, 1).weekday() == SAT:
            self[date(year, DEC, 25) + rd(days=-1)] = "Natal (Observed)"


class AR(Argentina):
    pass


class ARG(Argentina):
    pass
