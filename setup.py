import sys
from setuptools import setup, find_packages


if sys.version_info < (3,8,3):
    sys.exit("Wersje Python'a poniżej 3.8.3 nie są wspierane przez ten projekt")

include_package_data = True
setup(
   name='BombSweeperGame_PO_RS',
   version='1.0.0',
   author='Rafal Starypan',
   author_email='rafalstarypan@gmail.com',
   packages=find_packages('src'),
   license='MIT',
   description='Bombsweeper',
   long_description='Zaliczeniowy projekt - programowanie obiektowe - Rafał Starypan - Uniwersytet Wrocławski 2022',
   install_requires=[
       "pygame == 2.1.2",
   ],
   python_requires='>=3.8.3, <=3.8.13'
)