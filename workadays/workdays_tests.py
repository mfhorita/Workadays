# coding=utf-8

import os
import datetime as dt
from workadays import workdays as wd


def exec_tests():
    dt_ini = dt.date(2020, 12, 25)
    dt_fim = dt.date(2026, 12, 25)
    print(wd.networkdays(dt_ini, dt_fim))

    dt_ini = dt.date(2023, 5, 22)
    print(wd.workdays(dt_ini, 2520))

    dt_ini = dt.date(2023, 5, 22)
    data_hora = dt.datetime.combine(dt_ini, dt.time())
    print(wd.workdays(data_hora, 2520))

    for date in wd.get_holidays(country='England', years=range(2000, 2100)):
        print(date)

    # Dias corridos
    print('---------------------------------------------------------------------------------------------------')
    print('Data: 2020-12-25, Parâmetro D0: 2020-12-25, Parâmetro D+1: 2020-12-28, Parâmetro D-1: 2020-12-24')
    print('---------------------------------------------------------------------------------------------------')

    date = dt.date(2020, 12, 25)
    dt_zero = wd.workdays(date, 0)
    dt_proxdu = wd.workdays(date, 1)
    dt_duant = wd.workdays(date, -1)
    try:
        assert dt_zero == dt.date(2020, 12, 25)
        assert dt_proxdu == dt.date(2020, 12, 28)
        assert dt_duant == dt.date(2020, 12, 24)
        print('Testes da função de dias úteis.. OK!')
    except AssertionError as ex:
        print('Testes da função de dias úteis.. ERRO..')
        print('..Resultado esperado', date, dt_zero, dt_proxdu, dt_duant, ex)
        print('..Resultado esperado', '2020-12-25 2020-12-25 2020-12-28 2020-12-24', ex)
    print('---------------------------------------------------------------------------------------------------')
    print('')

    d1 = dt.date(2018, 1, 7)
    d2 = dt.date(2020, 12, 31)

    # Dias corridos
    resp = wd.days(d1, d2)
    try:
        assert resp == 1089
        print('Teste dias corridos.. OK!')
    except AssertionError as ex:
        print('Teste dias corridos.. ERRO:..')
        print('..Resultado {0}. O resultado esperado era 1089!'.format(resp), ex)

    # Dias corridos, base 30U/360 (método americano)
    resp = wd.days360(d1, d2, method_eu=False)
    try:
        assert resp == 1074
        print('Teste dias corridos, base 30U/360.. OK!')
    except AssertionError as ex:
        print('Teste dias corridos, base 30U/360.. ERRO:..')
        print('..Resultado {0}. O resultado esperado era 1074!'.format(resp), ex)

    # Dias corridos, base 30E/360 (método europeu)
    resp = wd.days360(d1, d2, method_eu=True)
    try:
        assert resp == 1073
        print('Teste dias corridos, base 30E/360.. OK!')
    except AssertionError as ex:
        print('Teste dias corridos, base 30E/360.. ERRO:..')
        print('..Resultado {0}. O resultado esperado era 1073!'.format(resp), ex)

    # Diferença de dias úteis entre duas datas
    resp = wd.networkdays(d1, d2)
    try:
        assert resp == 750
        print('Teste diferença de dias úteis com calendário brasileiro.. OK!')
    except AssertionError as ex:
        print('Teste diferença de dias úteis com calendário brasileiro.. ERRO:..')
        print('..Resultado {0}. O resultado esperado era 750!'.format(resp), ex)

    # Diferença de dias úteis entre duas datas sem calendário de feriados
    # (considera apenas os finais de semana como dia não útil)
    resp = wd.networkdays(d1, d2, country=None)
    try:
        assert resp == 779
        print('Teste diferença de dias úteis sem calendário nenhum.. OK!')
    except AssertionError as ex:
        print('Teste diferença de dias úteis sem calendário nenhum.. ERRO:..')
        print('..Resultado {0}. O resultado esperado era 779!'.format(resp), ex)

    # Soma 252 dias úteis com calendário de feriados padrão do Brasil
    resp = wd.workdays(d1, 252)
    date = dt.date(2019, 1, 9)
    try:
        assert resp == date
        print('Teste de soma de dias úteis com calendário brasileiro.. OK!')
    except AssertionError as ex:
        print('Teste de soma de dias úteis com calendário brasileiro.. ERRO:..')
        print('..Resultado {0}. O resultado esperado era {1}!'.format(resp, date), ex)

    # Soma 252 dias úteis sem calendário de feriados do Brasil
    # (considera apenas os finais de semana como dia não útil)
    resp = wd.workdays(d1, 252, country=None)
    date = dt.date(2018, 12, 25)
    try:
        assert resp == date
        print('Teste de soma de dias úteis sem calendário nenhum.. OK!')
    except AssertionError as ex:
        print('Teste de soma de dias úteis sem calendário nenhum.. ERRO:..')
        print('..Resultado {0}. O resultado esperado era {1}!'.format(resp, date), ex)

    # Verifica se é feriado
    date = dt.date(2020, 12, 24)
    resp = wd.is_holiday(date, country='BR')
    try:
        assert resp is False
        print('Teste para verificar se 24/12/2020 é feriado.. OK!')
    except AssertionError as ex:
        print('Teste para verificar se 24/12/2020 é feriado.. ERRO:..')
        print('..Resultado {0}. {1} não é feriado!'.format(resp, date), ex)

    # Verifica se é final de semana
    date = dt.date(2020, 12, 26)
    resp = wd.is_weekend(date)
    try:
        assert resp is True
        print('Teste para verificar se 26/12/2020 é fim de semana.. OK!')
    except AssertionError as ex:
        print('Teste para verificar se 26/12/2020 é fim de semana.. ERRO:..')
        print('..Resultado {0}. {1} é final de semana!'.format(resp, date), ex)

    # Verifica se é dia útil
    date = dt.date(2020, 12, 24)
    resp = wd.is_workday(date, country='BR')
    try:
        assert resp is True
        print('Teste para verificar se 24/12/2020 é dia útil.. OK!')
    except AssertionError as ex:
        print('Teste para verificar se 24/12/2020 é dia útil.. ERRO:..')
        print('ERRO: Resultado {0}. {1} é dia útil!'.format(resp, date), ex)

    # Verifica se é ano bissexto
    ano = 2010
    resp = wd.is_leap_year(ano)
    try:
        assert resp is False
        print('Teste para verificar se 2010 é ano bissexto.. OK!')
    except AssertionError as ex:
        print('Teste para verificar se 2010 é ano bissexto.. ERRO:..')
        print('ERRO: Resultado {0}. {1} não é ano bissexto!'.format(resp, ano), ex)

    os.system("pause")
    os.system("cls") or None

    print('')
    print('---------------------------------------------------------------------------------------------------')
    print(' LISTA DE FERIADOS NACIONAIS BRASILEIROS E MUNICIPAIS DE SÃO PAULO - ENTRE 2020 e 2021')
    print('---------------------------------------------------------------------------------------------------')
    for date in wd.get_holidays(country='BR', state='SP', years=range(2020, 2022)):
        print(date)

    os.system("pause")
    os.system("cls") or None

    print('')
    print('---------------------------------------------------------------------------------------------------')
    print(' LISTA DE FERIADOS DE LUXEMBURGO - ENTRE 2020 e 2021')
    print('---------------------------------------------------------------------------------------------------')
    for date in wd.get_holidays(country='LU', years=range(2020, 2022)):
        print(date)

    os.system("pause")
    os.system("cls") or None

    print('')
    print('---------------------------------------------------------------------------------------------------')
    print(' LISTA DE FERIADOS DE ESTADOS UNIDOS - ENTRE 2020 e 2025')
    print('---------------------------------------------------------------------------------------------------')
    for date in wd.get_holidays(country='US', years=range(2020, 2026)):
        print(date)

    os.system("pause")
    os.system("cls") or None

    print('')
    print('---------------------------------------------------------------------------------------------------')
    print(' LISTA DE FERIADOS DE REINO UNIDO - ENTRE 2020 e 2021')
    print('---------------------------------------------------------------------------------------------------')
    for date in wd.get_holidays(country='UK', years=range(2020, 2022)):
        print(date)

    os.system("pause")
    os.system("cls") or None

    print('')
    print('---------------------------------------------------------------------------------------------------')
    print(' LISTA DE FERIADOS DA INGLATERRA - ENTRE 2019 e 2022')
    print(" DIAS SEM DIVULGAÇÃO DAS LIBOR'S (EUR, USD, CHF, GBP, JPY) - FONTE ICE (INTERCONTINENTAL EXCHANCE)")
    print('---------------------------------------------------------------------------------------------------')
    for date in wd.get_holidays(country='England', years=range(2019, 2023)):
        print(date)

    os.system("pause")
    os.system("cls") or None


if __name__ == '__main__':
    exec_tests()
