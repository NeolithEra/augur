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

# Get the long description from the README file
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, './augur/VERSION'), encoding='utf-8') as f:
    version = f.read()

setup(
    name='augur',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description='A library for extracting actionable data from development tools ',
    long_description=long_description,

    # The project's main homepage.
    url='https://ua.github.com/deviant/augur',

    # Author details
    author='Karim Shehadeh',
    author_email='kshehadeh@underarmour.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='metrics jira github development',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'pony==0.7.3',
        'arrow==0.7.0',
        'boto3==1.2.6',
        'botocore==1.4.49',
        'jira==1.0.9.dev67',
        'Mako==1.0.3',
        'oauthlib==1.0.3',
        'pathspec==0.3.4',
        'pyfluence',
        'PyGithub==1.27.1',
        'python-dateutil==2.5.3',
        'pytz==2015.7',
        'urllib3==1.21.1',
        'psycopg2==2.6.1',
        'PyYAML==3.12',
        'munch==2.2.0',
        'pandas==0.22.0'
    ],

    dependency_links=[
       "https://pypi.python.org/simple/",
       "http://example2.com/p/bar-1.0.tar.gz",
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        '': [
            'data/*.*',
            'templates/*.*',
            'VERSION'
        ],
    },

    # Probably not necessary but trying it out anyway
    # include_package_data=True,

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)