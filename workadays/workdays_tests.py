# coding=utf-8

import datetime as dt
from workadays import workdays as wd

date = dt.date(2020, 12, 23)
dt_zero = wd.workdays(date, 0)
dt_proxdu = wd.workdays(date, 1)
dt_duant = wd.workdays(date, -1)
print(date, dt_zero, dt_proxdu, dt_duant)

date = dt.date(2020, 12, 24)
dt_zero = wd.workdays(date, 0)
dt_proxdu = wd.workdays(date, 1)
dt_duant = wd.workdays(date, -1)
print(date, dt_zero, dt_proxdu, dt_duant)

date = dt.date(2020, 12, 25)
dt_zero = wd.workdays(date, 0)
dt_proxdu = wd.workdays(date, 1)
dt_duant = wd.workdays(date, -1)
print(date, dt_zero, dt_proxdu, dt_duant)

date = dt.date(2020, 12, 26)
dt_zero = wd.workdays(date, 0)
dt_proxdu = wd.workdays(date, 1)
dt_duant = wd.workdays(date, -1)
print(date, dt_zero, dt_proxdu, dt_duant)

date = dt.date(2020, 12, 27)
dt_zero = wd.workdays(date, 0)
dt_proxdu = wd.workdays(date, 1)
dt_duant = wd.workdays(date, -1)
print(date, dt_zero, dt_proxdu, dt_duant)

date = dt.date(2020, 12, 28)
dt_zero = wd.workdays(date, 0)
dt_proxdu = wd.workdays(date, 1)
dt_duant = wd.workdays(date, -1)
print(date, dt_zero, dt_proxdu, dt_duant)

date = dt.date(2020, 12, 29)
dt_zero = wd.workdays(date, 0)
dt_proxdu = wd.workdays(date, 1)
dt_duant = wd.workdays(date, -1)
print(date, dt_zero, dt_proxdu, dt_duant)
print('')

d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)

# Dias corridos
print(wd.days(d1, d2))                          # 1089

# Dias corridos, base 30/360
print(wd.days360(d1, d2))                       # 1074

# Diferença de dias úteis entre duas datas
print(wd.networkdays(d1, d2))                   # 750

# Diferença de dias úteis entre duas datas sem calendário de feriados
# (considera apenas os finais de semana como dia não útil)
print(wd.networkdays(d1, d2, country=None))     # 779

# Soma 252 dias úteis com calendário de feriados padrão do Brasil
print(wd.workdays(d1, 252))                     # 09/01/2019

# Soma 252 dias úteis sem calendário de feriados do Brasil
# (considera apenas os finais de semana como dia não útil)
print(wd.workdays(d1, 252, country=None))       # 25/12/2018

# Soma 252 dias úteis a data de referência utilizando o calendário Brasil
print(wd.workdays(d1, 252, country='BR', years=range(2018, 2079)))

# Soma 252 dias úteis a data de referência utilizando o calendário Brasil e de SP
print(wd.workdays(d1, 252, country='BR', state='SP', years=range(2020, 2021)))

# Verifica se é feriado
d1 = dt.date(2020, 12, 24)
print('É feriado? ', wd.is_holiday(d1, country='BR', years=range(2020, 2021)))

# Verifica se é final de semana
print('É final de semana? ', wd.is_weekend(d1))

# Verifica se é dia útil
print('É dia útil? ', wd.is_workday(d1, country='BR', years=range(2020, 2021)))
print('')

# Busca lista de feriados referente ao calendário Brasil e de SP combinados
for date in wd.get_holidays(country='BR', state='SP', years=range(2018, 2019)):
    print(date)
