## Workadays:
#### Pacote para adicionar ou subtrair datas em dias úteis. A princípio eu escolhi focar apenas em alguns países: Brasil, Estados Unidos e Luxemburgo. No entanto, precisando de incluir novos países, estados ou regiões, será um prazer.


### Calendário de dias úteis:

```
import datetime as dt
import workadays as wd
```

### Dias corridos
```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)

print(wd.days(d1, d2))      # 1089
```

### Dias corridos, base 30/360
```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)

print(wd.days360(d1, d2))   # 1074
```

### Diferença de dias úteis entre duas datas
```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)

print(wd.networkdays(d1, d2))   # 750
```

### Diferença de dias úteis entre duas datas
### considerando apenas os finais de semana

```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)

print(wd.networkdays(d1, d2, country=None))   # 779
```

### Soma 252 dias úteis a data de referência utilizando o calendário Brasil
```
print(wd.workdays(date, 252, country='BR', years=range(2018, 2079)))
```

### Soma 252 dias úteis a data de referência utilizando o calendário Brasil e de SP
```
print(wd.workdays(date, 252, country='BR', state='SP', years=range(2018, 2079)))
```

### Exibe a lista de feriados
```
for date in wd.get_holidays(country='BR', state='SP', years=range(2020, 2021)):
    print(date)
```
