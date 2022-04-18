from numpy import find_common_type
from setuptools import setup, find_packages

requires = ['tornado']

setup(
    name='pellonvartija',
    version='0.0',
    description='',
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'serve = pellonvartija:main'
        ],
    },

)