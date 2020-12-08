# coding=utf-8

import datetime as dt
from workadays import workdays as wd


d1 = dt.date(2015, 2, 2)
d2 = dt.date(2018, 1, 1)

# Dias corridos
print(wd.days(d1, d2))     # 1064

# Dias corridos, base 30/360
print(wd.days360(d1, d2))  # 1049


date = dt.date(2018, 2, 14)

# Soma 252 dias úteis a data de referência utilizando o calendário Brasil
print(wd.workdays(date, 252, country='BR', years=range(2018, 2079)))
print('')

# Soma 252 dias úteis a data de referência utilizando o calendário Brasil e de SP
print(wd.workdays(date, 252, country='BR', state='SP', years=range(2020, 2021)))
print('')

# Verifica se é dia útil
print(wd.is_holiday(date, country='BR', years=range(2020, 2021)))
print('')

# Busca lista de feriados
for date in wd.get_holidays(country='BR', state='SP', years=range(2020, 2021)):
    print(date)
