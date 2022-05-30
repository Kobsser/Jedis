"""
MIT License

Copyright (c) 2022 Kobsser
"""

from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='jedis',
    version='0.1.0',
    description="An easy way to manage data in json",
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Kobsser/Jedis',
    author='Kobsser',
    author_email='devmoein@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='json python redis jedis PyJedis Kobsser easy-json easy simple easy-json-manipulation manager',
    packages=find_packages(),
    install_requires=[]
)