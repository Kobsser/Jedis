"""
MIT License

Copyright (c) 2021 Kobsser
"""

from setuptools import setup, find_packages

# See note below for more information about classifiers
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='jedis',
    version='0.0.4.2',
    description="Code Json like redis. it is PyJedis",
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/Kobsser/Jedis',  # the URL of your package's home page e.g. github link
    author='Kobsser',
    author_email='devmoein@gmail.com',
    license='MIT',  # note the American spelling
    classifiers=classifiers,
    keywords='json python redis jedis PyJedis Kobsser easy-json easy',  # used when people are searching for a module, keywords separated with a space
    packages=find_packages(),
    install_requires=[]  # a list of other Python modules which this module depends on.  For example RPi.GPIO
)