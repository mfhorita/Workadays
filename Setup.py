# coding=UTF-8

from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='workadays',
    version='2020.12.11',
    author='Marcelo Horita',
    author_email='mfhorita@gmail.com.br',
    packages=['workadays'],
    description='Calendário de dias úteis, dias corridos e dias 360 (30/360)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mfhorita',
    license='MIT',
    keywords='workdays workadays feriados holidays diasuteis uteis, dias360, days360, days',
    classifiers=[
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    install_requires=[
        'python_dateutil>=2.8.0',
        'six>=1.11.0'
    ]

)
