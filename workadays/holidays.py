# coding=utf-8

import inspect
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
