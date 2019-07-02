from pathlib import Path
from setuptools import setup, find_packages

setup(
    name='losovatko',
    version='0.1',
    description='A vocabulary picker',
    long_description=Path('README.md').read_text(),
    author='Petra Machackova',
    author_email='machackovapet@gmail.com',
    license='GPLv3',
    url='https://github.com/pindruska/losovatko',
    packages=['losovatko'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
    package_data={
        'losovatko': ['*.ui', 'slovicka*.txt'],

    },
    install_requires=[
        'PyQt5',
        'importlib_resources',
    ],
    entry_points={
        'console_scripts': [
            'losovatko = losovatko:main',
        ],
    },
)