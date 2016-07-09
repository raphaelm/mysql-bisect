from setuptools import setup

setup(
    name='mysqlbisect',
    version='1.0',
    py_modules=['mysqlbisect'],
    install_requires=[
        'Click',
        'mysqlclient'
    ],
    entry_points='''
[console_scripts]
mysqlbisect=mysqlbisect:bisect
    ''',
)
