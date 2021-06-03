# coding=UTF-8

from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='workadays',
    version='2021.06.03',
    author='Marcelo Horita',
    author_email='mfhorita@gmail.com.br',
    packages=['workadays'],
    description="Calendário de dias úteis, dias corridos e dias 360 (30/360). "
                "Há calendários de feriados do Brasil, Estados Unidos, Luxemburgo e Reino Unido. "
                "Reino Unido (UK, GB, GBR, England, Wales, Scotland, IsleOfMan, NorthernIreland). "
                "Utilize o calendário England para as Libor's (EUR, USD, CHF, GBP e JPY).",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mfhorita',
    license='MIT License',
    keywords='workdays workadays feriados holidays diasuteis uteis, dias360, days360, days',
    classifiers=[
        'License :: Freeware',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: Portuguese (Brazilian)',
        'Intended Audience :: Developers',
        'Topic :: Utilities'],
    install_requires=[
        'python_dateutil>=2.8.0',
        'six>=1.11.0'
    ]

)
