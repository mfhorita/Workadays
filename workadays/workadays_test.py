# coding=utf-8
import datetime as dt
import workadays as wd


date = dt.date(2018, 2, 14)

# Soma 252 dias úteis a data de referência utilizando o calendário Brasil
print(wd.workdays(date, 252, country='BR', years=range(2018, 2079)))
print('')

# Soma 252 dias úteis a data de referência utilizando o calendário Brasil e de SP
print(wd.workdays(date, 252, country='BR', state='SP', years=range(2018, 2079)))
print('')

# Verifica se é dia útil
print(wd.is_holiday(date, country='BR', years=range(2018, 2079)))
print('')

# Busca lista de feriados
for date in wd.get_holidays(country='BR', state='SP', years=range(2018, 2079)):
    print(date)
