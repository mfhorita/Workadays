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

