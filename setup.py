from setuptools import setup, find_namespace_packages

from pytonik_curl import Version

with open("README.md", "r") as fd:
    longdescription = fd.read()



setup(
    name='pytonik curl',
    version = Version.VERSION_TEXT+Version.EDITION,
    description='pytonik curl is built to transfer data using various network protocols and support sending or initiating actions within or outside protocols.',
    url="https://pytonik-curl.readthedocs.io",
    author='pytonik',
    author_email='info@pytonik.com',
    maintainer= 'Emmanuel Essien',
    maintainer_email='emmamartinscm@gmail.com',
    packages=find_namespace_packages(include=['*', '']),
    long_description = longdescription,
    long_description_content_type='text/markdown',
    license= Version.LICENSE,
    keywords = Version.KEYWORDS,   
                
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Topic :: Office/Business',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python'
    ],
    python_requires='>=2.7, >=2.7.*, >=3.*',
)
