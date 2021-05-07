from setuptools import setup, find_packages
 
setup(
    # 배포할 패키지의 이름을 적어줍니다. setup.py파일을 가지는 폴더 이름과 동일하게 합니다.
    name                = 'random_value',
    # 배포할 패키지의 버전을 적어줍니다. 첫 등록이므로 0.1 또는 0.0.1을 사용합니다.
    version             = '0.0.1',
    # 배포할 패키지에 대한 설명을 작성합니다.
    description         = 'This package returns random values.',
    # 배포하는 사람의 이름을 작성합니다.
    author              = 'jjun4341',
    author_email        = 'rhwldns@naver.com',
    url                 = 'https://github.com/jjun4341/random_value',
    download_url        = 'https://github.com/jjun4341/random_value/src/random_value/random_value.py',
    install_requires    =  ['string'],
    packages            = find_packages(exclude = []),
    # 패키지의 키워드를 적습니다.
    keywords            = ['pypi deploy'],
    # 해당 패키지를 사용하기 위해 필요한 파이썬 버전을 적습니다.
    python_requires     = '>=3',
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


출처: https://doorbw.tistory.com/225 [Tigercow.Door]