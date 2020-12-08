## Workadays:
#### Pacote para adicionar ou subtrair datas em dias �teis. A princ�pio eu escolhi focar apenas em alguns pa�ses: Brasil, Estados Unidos e Luxemburgo. No entanto, precisando de incluir novos pa�ses, estados ou regi�es, ser� um prazer.


### Calend�rio de dias �teis:

```
import workadays as wd
```

```
import datetime as dt
date = dt.date(2018, 2, 14)
```

### Soma 252 dias �teis a data de refer�ncia utilizando o calend�rio Brasil
```
print(wd.workdays(date, 252, country='BR', years=range(2018, 2079)))
```

### Soma 252 dias �teis a data de refer�ncia utilizando o calend�rio Brasil e de SP
```
print(wd.workdays(date, 252, country='BR', state='SP', years=range(2018, 2079)))
```

### Verifica se � dia �til
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
