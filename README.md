## Workadays:
#### Pacote para adicionar ou subtrair datas em dias �teis. A princ�pio eu escolhi focar apenas em alguns pa�ses: Brasil, Estados Unidos e Luxemburgo. No entanto, precisando de incluir novos pa�ses, estados ou regi�es, ser� um prazer.


### Calend�rio de dias �teis:

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

### Diferen�a de dias �teis entre duas datas
```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)

print(wd.networkdays(d1, d2))   # 750
```

### Diferen�a de dias �teis entre duas datas
### considerando apenas os finais de semana

```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)

print(wd.networkdays(d1, d2, country=None))   # 779
```

### Soma 252 dias �teis a data de refer�ncia utilizando o calend�rio Brasil
```
print(wd.workdays(date, 252, country='BR', years=range(2018, 2079)))
```

### Soma 252 dias �teis a data de refer�ncia utilizando o calend�rio Brasil e de SP
```
print(wd.workdays(date, 252, country='BR', state='SP', years=range(2018, 2079)))
```

### Exibe a lista de feriados
```
for date in wd.get_holidays(country='BR', state='SP', years=range(2020, 2021)):
    print(date)
```
