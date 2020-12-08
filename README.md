## Workadays:
#### Pacote para adicionar ou subtrair datas em dias úteis. A princípio eu escolhi focar apenas em alguns países: Brasil, Estados Unidos e Luxemburgo. No entanto, precisando de incluir novos países, estados ou regiões, será um prazer.


### Calendário de dias úteis:

```
import workadays as wd
```

```
import datetime as dt
date = dt.date(2018, 2, 14)
```

### Soma 252 dias úteis a data de referência utilizando o calendário Brasil
```
print(wd.workdays(date, 252, country='BR', years=range(2018, 2079)))
```

### Soma 252 dias úteis a data de referência utilizando o calendário Brasil e de SP
```
print(wd.workdays(date, 252, country='BR', state='SP', years=range(2018, 2079)))
```

### Verifica se é dia útil
```
print(wd.is_holiday(date, country='BR', years=range(2018, 2079)))
```

### Dias corridos
```
d1 = dt.date(2015, 2, 2)
d2 = dt.date(2018, 1, 1)

print(wd.days(d1, d2))      # 1064
```

### Dias corridos, base 30/360
```
d1 = dt.date(2015, 2, 2)
d2 = dt.date(2018, 1, 1)

print(wd.days360(d1, d2))   # 1049
```
