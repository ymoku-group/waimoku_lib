from os import path
from setuptools import setup
from setuptools import find_packages


def read(file_name: str):
    """ファイルの内容を読み込む

    Arguments:
        fname {str} -- ファイル名

    Returns:
        [type] -- 読み込んだファイルの内容
    """
    return open(path.join(path.dirname(__file__), file_name)).read()


setup(
    name='waimoku',
    version='0.0.4',
    description='ワイもくのConnpasで取得しているアンケートから運営に必要な情報を抽出するPythonのScript です。',
    long_description=read("README.rst"),
    author='Atsuki Seo',
    maintainer='Atsuki Seo',
    install_requires=["pandas", "openpyxl"],
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'
    ],
    packages=find_packages(),
    package_data={
        "waimoku": ["res/*.xlsx"]
    },
    entry_points={
        'console_scripts': [
            'waimoku = waimoku.main:main',
        ],
    },
)
