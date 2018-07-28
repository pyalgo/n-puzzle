from setuptools import setup, find_packages


packages = find_packages()
description = 'Cli utility to solve n-puzzle problem'
author = 'Serhii Ladonia, Olexandr Baranov'
author_email = 'ladonya.s@gmail.com'
url = 'https://github.com/pyalgo/n-puzzle'


setup(
    name='n-puzzle',
    version='0.1',
    description=description,
    long_description=description,
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    url=url,
    license='MIT',
    packages=packages,
    entry_points={
        'console_scripts': ['npuzzle=n-puzzle.main:main'],
    }
)
