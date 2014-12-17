from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'readme.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bencher',
    version='0.0.1',
    description='A Benchmarking tool',
    long_description=long_description,
    url='https://github.com/danielscottt/bencher',
    author='dan pittman',
    author_email='danielscottt@gmail.com',
    license='MIT',
    keywords='benchmarking benchmark development',
    packages=find_packages(exclude=['tests*']),
)
