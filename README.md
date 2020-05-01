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

