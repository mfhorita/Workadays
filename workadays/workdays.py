# coding=utf-8

import datetime as dt
from workadays import holidays as hl


def get_holidays(years=None, expand=True, observed=True, country='BR', prov=None, state=None):

    if years is None:
        years = [2020]

    holidays = []
    for holiday in sorted(hl.CountryHoliday(country=country, prov=prov, state=state,
                                            years=years, expand=expand, observed=observed).items()):
        holidays.append(holiday[0])

    return sorted(holidays)


def workdays(start_date=dt.datetime.today().date(), ndays=0,
             years=None, expand=True, observed=True, country='BR', prov=None, state=None):

    if years is None:
        years = [2020]

    holidays = get_holidays(years=years, expand=expand, observed=observed,
                            country=country, prov=prov, state=state)

    dt_aux = start_date
    dt_fim = start_date + dt.timedelta(ndays)
    if ndays >= 0:
        while dt_aux <= dt_fim:

            if dt_aux.weekday() >= 6:
                dt_fim += dt.timedelta(1)  # Soma 1 dia se for domingo
                dt_aux += dt.timedelta(1)
            elif dt_aux.weekday() >= 5:
                dt_fim += dt.timedelta(2)  # Soma 2 dias se for sábado
                dt_aux += dt.timedelta(2)
            else:
                if dt_aux in holidays:
                    dt_fim += dt.timedelta(1)  # Soma 1 dia se for feriado

                dt_aux += dt.timedelta(1)

    elif ndays < 0:
        while dt_aux >= dt_fim:

            if dt_aux.weekday() >= 6:
                dt_fim -= dt.timedelta(2)       # Tira 2 dias se for domingo
                dt_aux -= dt.timedelta(2)
            elif dt_aux.weekday() >= 5:
                dt_fim -= dt.timedelta(1)       # Tira 1 dia se for sábado
                dt_aux -= dt.timedelta(1)
            else:
                if dt_aux in holidays:
                    dt_fim -= dt.timedelta(1)   # Tira 1 dia se for feriado

                dt_aux -= dt.timedelta(1)

    return dt_fim


def is_holiday(date=dt.datetime.today().date(),
               years=None, expand=True, observed=True, country='BR', prov=None, state=None):

    if years is None:
        years = [2020]

    holidays = get_holidays(years=years, expand=expand, observed=observed,
                            country=country, prov=prov, state=state)
    return date in holidays


def days360(start_date=dt.date(dt.datetime.today().year, dt.datetime.today().month, dt.datetime.today().day),
            end_date=dt.date(dt.datetime.today().year, dt.datetime.today().month, dt.datetime.today().day),
            method_eu=False):

    start_day = start_date.day
    start_month = start_date.month
    start_year = start_date.year
    end_day = end_date.day
    end_month = end_date.month
    end_year = end_date.year

    if (
        start_day == 31 or
        (
            method_eu is False and
            start_month == 2 and (
                start_day == 29 or (
                    start_day == 28 and
                    start_date.is_leap_year is False
                )
            )
        )
    ):
        start_day = 30

    if end_day == 31:
        if method_eu is False and start_day != 30:
            end_day = 1

            if end_month == 12:
                end_year += 1
                end_month = 1
            else:
                end_month += 1
        else:
            end_day = 30

    return (
        end_day + end_month * 30 + end_year * 360 -
        start_day - start_month * 30 - start_year * 360)


def days(start_date=dt.datetime.today().date(), end_date=dt.datetime.today().date()):
    return (end_date - start_date).days     # retorna dias corridos
