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


def workdays(start_date=dt.datetime.today().date(), days=0,
             years=None, expand=True, observed=True, country='BR', prov=None, state=None):

    if years is None:
        years = [2020]

    holidays = get_holidays(years=years, expand=expand, observed=observed,
                            country=country, prov=prov, state=state)

    dt_aux = start_date
    dt_fim = start_date + dt.timedelta(days)
    if days >= 0:
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

    elif days < 0:
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
