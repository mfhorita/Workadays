# coding=utf-8

import inspect
import datetime as dt
from workadays import countries


def list_supported_countries():
    """List all supported countries incl. their abbreviation."""
    return [name for name, obj in
            inspect.getmembers(countries, inspect.isclass)]


def CountryHoliday(country, years=None, prov=None, state=None, expand=True, observed=True):

    if years is None:
        years = range(1900, 2100)

    try:
        country_classes = inspect.getmembers(countries, inspect.isclass)
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
