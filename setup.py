# coding: utf-8

from setuptools import setup
from flask_gladiator import get_version


def read_file(f):
    with open(f, 'r') as _file:
        return _file.read()


setup(
    name='Flask-Gladiator',
    version=get_version(),
    url='https://github.com/laco/flask-gladiator',
    download_url='https://github.com/laco/flask-gladiator/tarball/' + get_version(),
    license='BSD',
    author='László Andrási',
    author_email='mail@laszloandrasi.com',
    description='Gladiator is a Data Validation Framework for Python3 (Flask Plugin)',
    long_description=read_file('README.rst') + '\n\n',
    packages=['flask_gladiator'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['Flask', 'Gladiator'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
