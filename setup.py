from setuptools import setup, find_packages


setup(

    name                = 'randomvalue',
    version             = '110',
    description         = 'This package returns random values.',
    author              = 'jjun4341',
    author_email        = 'rhwldns@naver.com',
    url                 = 'https://github.com/jjun4341/random_value',
    download_url        = 'https://github.com/jjun4341/random_value/src/random_value/random_value.py',
    install_requires    =  [],
    keywords            = ['pypi deploy'],
    python_requires     = '>=3',
    long_description=open('README.md', encoding='UTF-8').read(),
    long_description_content_type='text/markdown',
    packages            = ['randomvalue'],
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)


