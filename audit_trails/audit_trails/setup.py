"""The setup module for django_saml2_auth.
See:
https://github.com/fangli/django_saml2_auth
"""

from codecs import open
from setuptools import (setup, find_packages)
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django_audit_trial',

    version='1.0.1',

    description='Django Audits for logging the events and actions performed by the user and Admin.',
    long_description=long_description,

    url='https://github.com/fangli/django-saml2-auth',

    author='Manoj Kashyap',
    author_email='mkashyap@analyticalwizards.com',

    # license='Apache 2.0',

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 2.0',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],

    keywords='Django Audits for logging the events and actions performed by the user and Admin.',

    packages=find_packages(),

    install_requires=['django>=2.0'],
    include_package_data=True,
)