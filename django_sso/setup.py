import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-sso',
    version='0.3',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to conduct Web-based sso.',
    long_description=README,
    url='https://vpolepalli@bitbucket.org/aw-teams/python.git',
    author='Vpolepalli',
    author_email='vpolepalli@analyitcalwizards.com',
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
    install_requires=['pysaml2>=4.5.0',
                      'django>=2.0',
                      'djangorestframework-jwt',
                      'django-rest-auth', ],

)
