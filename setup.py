from setuptools import setup

import trakt

__author__ = 'Scott Willsey'

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()
with open('requirements.txt') as f:
    requires = [line.strip() for line in f if line.strip()]

packages = ['trakt']
description = ('Pythonic abstraction layer for easier scripting of the '
               'Trakt.tv REST API.')

setup(
    name='pytrakt',
    version=trakt.__version__,
    description=description,
    long_description='\n'.join([readme, history]),
    author='Scott Willsey',
    author_email='gallant_07_skull@icloud.com',
    url='https://github.com/scottaw66/python-pytrakt',
    packages=packages,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Freely Distributable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9']
)
