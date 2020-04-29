# coding=utf-8

import inspect
import workadays
import datetime as dt


def list_supported_countries():
    """List all supported countries incl. their abbreviation."""
    return [name for name, obj in
            inspect.getmembers(workadays.countries, inspect.isclass)]


def CountryHoliday(country, years=None, prov=None, state=None, expand=True, observed=True):

    if years is None:
        years = [2020]

    try:
        country_classes = inspect.getmembers(workadays.countries, inspect.isclass)
        country = next(obj for name, obj in country_classes if name == country)
        country_holiday = country(years=years, prov=prov, state=state,
                                  expand=expand, observed=observed)
    except StopIteration:
        raise KeyError("Country %s not available" % country)

    return country_holiday


def get_gre_date(year, month, day):
    """
    returns the gregian date of of a  of the given gregorian calendar
    yyyy year with Hijari Month & Day
    works *only* if hijri-converter library is installed, otherwise a warning
    is raised that this holiday is missing. hijri-converter requires
    Python >= 3.6
    """
    try:
        from hijri_converter import convert
    except ImportError:
        import warnings

        def warning_on_one_line(message, filename):
            return filename + ': ' + str(message) + '\n'

        warnings.formatwarning = warning_on_one_line
        warnings.warn("Error estimating Islamic Holidays." +
                      "To estimate, install hijri-converter library")
        warnings.warn("pip install -U hijri-converter")
        warnings.warn("(see https://hijri-converter.readthedocs.io/ )")

        return []

    year = convert.Gregorian(year, 1, 1).to_hijri().datetuple()[0]

    gres = [convert.Hijri(year - 1, month, day).to_gregorian(),
            convert.Hijri(year, month, day).to_gregorian(),
            convert.Hijri(year + 1, month, day).to_gregorian()]

    gre_dates = []
    for gre in gres:
        if gre.year == year:
            gre_dates.append(dt.date(*gre.datetuple()))
    return gre_dates


def get_holidays(years=None, expand=True, observed=True, country='BR', prov=None, state=None):

    if years is None:
        years = [2020]

    holidays = []
    for holiday in sorted(CountryHoliday(country=country, prov=prov, state=state,
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
