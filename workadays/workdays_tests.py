# coding=utf-8

import datetime as dt
from workadays import workdays as wd


d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)

# Dias corridos
print(wd.days(d1, d2))     # 1095

# Dias corridos, base 30/360
print(wd.days360(d1, d2))  # 1080

# Diferença de dias úteis entre duas datas
print(wd.networkdays(d1, d2))

# Diferença de dias úteis entre duas datas
# considerando apenas os finais de semana
print(wd.networkdays(d1, d2, country=None))

# Soma 252 dias úteis a data de
# referência utilizando o calendário Brasil
print(wd.workdays(d1, -50))

# Soma 252 dias úteis a data de
# referência utilizando o calendário Brasil
print(wd.workdays(d1, -50, country=None))

# Soma 252 dias úteis a data de referência utilizando o calendário Brasil
print(wd.workdays(d1, -50, country='BR', years=range(2018, 2079)))

# Soma 252 dias úteis a data de referência utilizando o calendário Brasil e de SP
print(wd.workdays(d1, -50, country='BR', state='SP', years=range(2020, 2021)))

# Verifica se é dia útil
print(wd.is_holiday(d1, country='BR', years=range(2020, 2021)))
print('')

# Busca lista de feriados
for date in wd.get_holidays(country='BR', state='SP', years=range(2020, 2021)):
    print(date)
