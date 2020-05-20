"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-upsource-api',

    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description='Jetbrains Upsource API handler for Python',
    long_description=long_description,
    url='https://github.com/shijl0925/python-upsource-api',
    author='Jialiang Shi',
    author_email='kevin09254930sjl@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development'
    ],

    keywords='api upsource hub',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),

    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'requests',
    ],
    extras_require={},
    package_data={},

    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    data_files=[],
)
