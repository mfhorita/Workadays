# coding=UTF-8

from setuptools import setup

setup(
    name='workadays',
    version='1.1.0',
    author='Marcelo Horita',
    author_email='datazeus.tecnologia@gmail.com.br',
    packages=['workadays'],
    description='Calendário de dias úteis',
    long_description='Pacote para adicionar ou subtrair datas em dias úteis',
    url='https://github.com/mfhorita',
    license='MIT',
    keywords='workdays',
    classifiers=[
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    install_requires=[
        'python_dateutil>=2.8.0',
        'six>=1.11.0',
        'convertdate>=2.2.0'
    ]

)
