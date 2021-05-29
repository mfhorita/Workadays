## Workadays:
#### Pacote para calcular dias úteis, dias corridos e dias na base 360. A base de feriados inicialmente implementados são: Brasil, Estados Unidos e Luxemburgo.


### Calendário de dias úteis:

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

### Diferença de dias úteis entre duas datas
```
print(wd.networkdays(d1, d2))                   # 750
```

### Diferença de dias úteis entre duas datas sem calendário de feriados (considera apenas os finais de semana como dia não útil)
```
print(wd.networkdays(d1, d2, country=None))     # 779
```

### # Soma 252 dias úteis com calendário de feriados padrão do Brasil
```
print(wd.workdays(d1, 252))                     # 09/01/2019
```

### Soma 252 dias úteis a data de referência utilizando o calendário Brasil e de SP
```
print(wd.workdays(d1, 252, country=None))       # 25/12/2018
```

### Verifica se é feriado
```
print('É feriado? ', wd.is_holiday(d1, country='BR', years=range(2020, 2021)))
```

### Verifica se é final de semana
```
print('É final de semana? ', wd.is_weekend(d1))
```

### Verifica se é dia útil
```
print('É dia útil? ', wd.is_workday(d1, country='BR', years=range(2020, 2021)))
```

### Verifica se é ano bissexto
```
print('É ano bissexto? ', wd.is_leap_year(2008)
```

### Exibe a lista de feriados
```
for date in wd.get_holidays(country='BR', state='SP', years=range(2020, 2021)):
    print(date)
```
