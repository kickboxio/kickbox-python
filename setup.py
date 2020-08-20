import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='kickbox',
    version='2.0.4',
    description='Official kickbox API library client for python',
    author='Chaitanya Surapaneni',
    author_email='chaitanya.surapaneni@kickbox.com',
    url='https://kickbox.com',
    license='MIT',
    install_requires=[
        'requests >= 2.1.0',
        'six >= 1.9.0'
    ],
    packages=[
        'kickbox',
        'kickbox.api',
        'kickbox.error',
        'kickbox.http_client'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
