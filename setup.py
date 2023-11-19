# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='geo_northarrow',
    version='v0.2.0-alpha',
    description='Python package of geo_northarrow for inserting north arrow polygons into geopandas, geoplot, matplotlib maps.',
    long_description=readme,
    author='Peter Scully',
    author_email='',
    url='https://github.com/pmdscully/geo_northarrow/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
