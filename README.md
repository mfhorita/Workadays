## Workadays:
#### Pacote para calcular dias �teis, dias corridos e dias na base 360. A base de feriados inicialmente implementados s�o: Brasil, Estados Unidos e Luxemburgo.


### Calend�rio de dias �teis:

```
import datetime as dt
from workadays import workadays as wd
```

### Dias corridos
```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)

print(wd.days(d1, d2))                          # 1089
```

### Dias corridos, base 30/360
```
print(wd.days360(d1, d2))                       # 1074
```

### Diferen�a de dias �teis entre duas datas
```
print(wd.networkdays(d1, d2))                   # 750
```

### Diferen�a de dias �teis entre duas datas sem calend�rio de feriados (considera apenas os finais de semana como dia n�o �til)
```
print(wd.networkdays(d1, d2, country=None))     # 779
```

### # Soma 252 dias �teis com calend�rio de feriados padr�o do Brasil
```
print(wd.workdays(d1, 252))                     # 09/01/2019
```

### Soma 252 dias �teis a data de refer�ncia utilizando o calend�rio Brasil e de SP
```
print(wd.workdays(d1, 252, country=None))       # 25/12/2018
```

### Verifica se � feriado
```
print('� feriado? ', wd.is_holiday(d1, country='BR', years=range(2020, 2021)))
```

### Verifica se � final de semana
```
print('� final de semana? ', wd.is_weekend(d1))
```

### Verifica se � dia �til
```
print('� dia �til? ', wd.is_workday(d1, country='BR', years=range(2020, 2021)))
```

### Verifica se � ano bissexto
```
print('� ano bissexto? ', wd.is_leap_year(2008)
```

### Exibe a lista de feriados
```
for date in wd.get_holidays(country='BR', state='SP', years=range(2020, 2021)):
    print(date)
```
