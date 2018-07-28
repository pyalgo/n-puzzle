from setuptools import setup, find_packages


packages = find_packages()
description = 'Cli utility to solve n_puzzle problem'
author = 'Serhii Ladonia, Olexandr Baranov'
author_email = 'ladonya.s@gmail.com'
url = 'https://github.com/pyalgo/n_puzzle'


setup(
    name='n_puzzle',
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
        'console_scripts': ['npuzzle=n_puzzle.main:main'],
    }
)
