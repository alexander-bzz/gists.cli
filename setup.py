#! /usr/bin/env python
#! -*- coding: utf-8 *-*-

from setuptools import setup, find_packages

readme = open('README.md', 'r').read()
setup(
    name='gistcommand',
    version='0.1',
    url='https://github.com/khilnani/gistcommand',
    license='GPLv2',
    author='khilnani',
    author_email='nik@khilnani.org',
    description='A CLI to create, edit, view and list GitHub Gists',
    include_package_data=True,
    long_description=readme,
    packages=find_packages(),
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'gists = gistcommand.gists:main',
            ]
    },
    classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',

    ],
    )
