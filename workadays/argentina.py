# -*- coding: utf-8 -*-

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, MO, FR, TU

from workadays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, OCT, NOV, DEC, SUN, TUE, WED, THU, FRI, SAT
from workadays.holiday_base import HolidayBase


class Argentina(HolidayBase):
    """
    https://pt.wikipedia.org/wiki/Feriados_na_Argentina
    https://www.argentina.gob.ar/interior/feriados-nacionales-2023
    """

    def __init__(self, **kwargs):
        self.country = 'AR'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, JAN, 1)] = "Año Nuevo"
        if date(year, JAN, 1).weekday() == TUE:
            self[date(year, JAN, 1) + rd(days=-1)] = "Año Nuevo (Observed)"
        elif date(year, JAN, 1).weekday() == THU:
            self[date(year, JAN, 1) + rd(days=+1)] = "Año Nuevo (Observed)"

        # Carnaval
        quaresma = easter(year) - rd(days=46)  # self[quaresma] = "Quarta-feira de cinzas (Início da Quaresma)"
        self[quaresma - rd(weekday=TU(-1)) - rd(days=1)] = "Carnaval"
        self[quaresma - rd(weekday=TU(-1))] = "Carnaval"

        # Día de la Verdad y la Justicia
        # Empezado en 1 August 2002
        if year > 2004:
            self[date(year, MAR, 24)] = "Día de la Verdad y la Justicia"
            if date(year, MAR, 24).weekday() == TUE:
                 self[date(year, MAR, 23)] = "Feriado Puente - Día de la Verdad y la Justicia"
            elif date(year, MAR, 24).weekday() == THU:
                 self[date(year, MAR, 25)] = "Feriado Puente - Día de la Verdad y la Justicia"

        # Empezado en 22 November 2000
        if year > 2000:
            if year == 2020:
                # El feriado del 2 de abril fue trasladado al día martes 31 de marzo de 2020, por única vez,
                # motivo del aislamiento obligatorio y preventivo en todo el país. Decreto 297/2020
                self[date(year, MAR, 31)] = "Malvinas Day"
            else:
                self[date(year, APR, 2)] = "Malvinas Day"

        # Páscoa
        self[easter(year) - rd(days=3)] = "Jueves Santo"
        self[easter(year) - rd(days=2)] = "Viernes Santo"
        # self[easter(year)] = "Páscoa"

        # Dia del Trabajo
        self[date(year, MAY, 1)] = "Día Internacional del Trabajo"

        # Census Day
        if year == 2022:
            self[date(year, MAY, 18)] = "Census Day"

        # Revolución de Mayo
        self[date(year, MAY, 25)] = "Revolución de Mayo"
        if date(year, MAY, 25).weekday() == TUE:
            self[date(year, MAY, 24)] = "Feriado Puente - Revolución de Mayo"
        elif date(year, MAY, 25).weekday() == THU:
            self[date(year, MAY, 26)] = "Feriado Puente - Revolución de Mayo"

        # Muerte del General Martín Miguel de Güemes
        if year > 2015:
            if self.observed and date(year, JUN, 17).weekday() == TUE:
                self[date(year, JUN, 17) + rd(days=-1)] = "Muerte del General Martín Miguel de Güemes (Observed)"
            elif self.observed and date(year, JUN, 17).weekday() == WED:
                self[date(year, JUN, 17) + rd(days=-2)] = "Muerte del General Martín Miguel de Güemes (Observed)"
            elif self.observed and date(year, JUN, 17).weekday() == THU:
                self[date(year, JUN, 17) + rd(days=+4)] = "Muerte del General Martín Miguel de Güemes (Observed)"
            # elif self.observed and date(year, JUN, 17).weekday() == FRI:
            #     self[date(year, JUN, 17) + rd(days=+3)] = "Muerte del General Martín Miguel de Güemes (Observed)"
            elif self.observed and date(year, JUN, 17).weekday() == SUN:
                self[date(year, JUN, 17) + rd(days=+1)] = "Muerte del General Martín Miguel de Güemes (Observed)"
            else:
                self[date(year, JUN, 17)] = "Muerte del General Martín Miguel de Güemes"

        # Flag Day
        if year > 1938:
            self[date(year, JUN, 20)] = "Flag Day"
            if self.observed and date(year, JUN, 20).weekday() == TUE:
                self[date(year, JUN, 20) + rd(days=-1)] = "Flag Day (Observed)"
            elif self.observed and date(year, JUN, 20).weekday() == WED:
                self[date(year, JUN, 20) + rd(days=-2)] = "Flag Day (Observed)"
            elif self.observed and date(year, JUN, 20).weekday() == THU:
                self[date(year, JUN, 20) + rd(days=+4)] = "Flag Day (Observed)"
            elif self.observed and date(year, JUN, 20).weekday() == FRI:
                self[date(year, JUN, 20) + rd(days=+3)] = "Flag Day (Observed)"

        # Día de la Independencia
        self[date(year, JUL, 9)] = "Día de la Independencia"
        if date(year, JUL, 9).weekday() == TUE:
            self[date(year, JUL, 8)] = "Feriado Puente - Día de la Independencia"
        elif date(year, JUL, 9).weekday() == THU:
            self[date(year, JUL, 10)] = "Feriado Puente - Día de la Independencia"

        # Dia Móvel (Tercera lunes del mês)
        self[date(year, AUG, 1) + rd(weekday=MO(3))] = "Muerte del general José de San Martín"

        # Día del Respeto a la Diversidad Cultural
        if self.observed and date(year, OCT, 12).weekday() == TUE:
            dt_cultura = date(year, OCT, 12) + rd(days=-1)
        elif self.observed and date(year, OCT, 12).weekday() == WED:
            dt_cultura = date(year, OCT, 12) + rd(days=-2)
        elif self.observed and date(year, OCT, 12).weekday() == THU:
            dt_cultura = date(year, OCT, 12) + rd(days=+4)
        elif self.observed and date(year, OCT, 12).weekday() == FRI:
            dt_cultura = date(year, OCT, 12) + rd(days=+3)
        elif self.observed and date(year, OCT, 12).weekday() == SAT:
            dt_cultura = date(year, OCT, 12) + rd(days=+2)
        elif self.observed and date(year, OCT, 12).weekday() == SUN:
            dt_cultura = date(year, OCT, 12) + rd(days=+1)
        else:
            dt_cultura = date(year, OCT, 12)
        self[dt_cultura] = "Flag Day (Observed)"

        # Feriado con fines turísticos
        if year > 2020:
            self[dt_cultura + rd(weekday=FR(-1))] = "Feriado con fines turísticos"

        # Día de la Soberanía Nacional
        if year > 2009:
            if self.observed and date(year, NOV, 20).weekday() == TUE:
                self[date(year, NOV, 20) + rd(days=-1)] = "Día de la Soberanía Nacional (Observed)"
            elif self.observed and date(year, NOV, 20).weekday() == WED:
                self[date(year, NOV, 20) + rd(days=-2)] = "Día de la Soberanía Nacional (Observed)"
            elif self.observed and date(year, NOV, 20).weekday() == THU:
                self[date(year, NOV, 20) + rd(days=+1)] = "Día de la Soberanía Nacional (Observed)"
            elif self.observed and date(year, NOV, 20).weekday() == FRI:
                self[date(year, NOV, 20) + rd(days=+3)] = "Día de la Soberanía Nacional (Observed)"
            elif self.observed and date(year, NOV, 20).weekday() == SAT:
                self[date(year, NOV, 20) + rd(days=+2)] = "Día de la Soberanía Nacional (Observed)"
            elif self.observed and date(year, NOV, 20).weekday() == SUN:
                self[date(year, NOV, 20) + rd(days=+1)] = "Día de la Soberanía Nacional (Observed)"
            else:
                self[date(year, NOV, 20)] = "Día de la Soberanía Nacional"

        # Inmaculada Concepción de María
        self[date(year, DEC, 8)] = "Inmaculada Concepción de María"
        if date(year, DEC, 8).weekday() == TUE:
            self[date(year, DEC, 7)] = "Feriado Puente - Inmaculada Concepción de María"
        elif date(year, DEC, 8).weekday() == THU:
            self[date(year, DEC, 9)] = "Feriado Puente - Inmaculada Concepción de María"

        # Christmas Day
        self[date(year, DEC, 24)] = "Víspera de Navidad"
        self[date(year, DEC, 25)] = "Navidad"
        if self.observed and date(year, DEC, 25).weekday() == THU:
            self[date(year, DEC, 25) + rd(days=+1)] = "Navidad (Observed)"


class AR(Argentina):
    pass


class ARG(Argentina):
    pass
