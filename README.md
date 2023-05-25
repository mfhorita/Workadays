## Workadays:
#### <h3>Pacote para calcular dias �teis, dias corridos e dias na base 360 (30/360).</h3>
H� calend�rios de feriados do Brasil, Estados Unidos, Luxemburgo e Reino Unido. <p>
Considera o novo feriado dos EUA, Juneteenth. Consulte: https://pt.wikipedia.org/wiki/Juneteenth <p>


### Calend�rio de dias �teis:

```
import datetime as dt
from workadays import workdays as wd
```

### Dias corridos
```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)
print(wd.days(d1, d2))                          # 1089
```

### Dias corridos, base 30U/360, m�todo americano 
```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)
print(wd.days360(d1, d2, method_eu=False))     # 1074
```

### Dias corridos, base 30E/360, m�todo europeu 
```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)
print(wd.days360(d1, d2, method_eu=True))     # 1073
```

### Diferen�a de dias �teis entre duas datas
```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)
print(wd.networkdays(d1, d2))                # 750
```

### Diferen�a de dias �teis entre duas datas sem calend�rio de feriados (considera apenas os finais de semana como dia n�o �til)
```
d1 = dt.date(2018, 1, 7)
d2 = dt.date(2020, 12, 31)
print(wd.networkdays(d1, d2, country=None))  # 779
```

### # Soma 252 dias �teis com calend�rio de feriados padr�o do Brasil
```
d1 = dt.date(2018, 1, 7)
print(wd.workdays(d1, 252))                  # 09/01/2019
```

### Soma 252 dias �teis a data de refer�ncia utilizando o calend�rio Brasil e de SP
```
d1 = dt.date(2018, 1, 7)
print(wd.workdays(d1, 252, country=None))    # 25/12/2018
```

### Verifica se � feriado
```
d1 = dt.date(2018, 1, 7)
print('� feriado? ', wd.is_holiday(d1, country='BR', years=range(2020, 2021)))
```

### Verifica se � final de semana
```
d1 = dt.date(2018, 1, 7)
print('� final de semana? ', wd.is_weekend(d1))
```

### Verifica se � dia �til
```
d1 = dt.date(2018, 1, 7)
print('� dia �til? ', wd.is_workday(d1, country='BR', years=range(2020, 2021)))
```

### Verifica se � ano bissexto
```
print('� ano bissexto? ', wd.is_leap_year(2008))
```

### Exibe a lista de feriados do Brasil e de S�o Paulo
```
for date in wd.get_holidays(country='BR', state='SP', years=range(2020, 2022)):
    print(date)
```

### Exibe a lista de feriados da Inglaterra e das Libor's
```
for date in wd.get_holidays(country='England', years=range(2019, 2023)):
    print(date)
```
