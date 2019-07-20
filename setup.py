from setuptools import setup
from setuptools import find_packages

setup(
    name='waimoku',
    version='0.0.2',
    description='PythonScript to convert "Waimoku" participant information into "Yahoo! LODGE" participant list file format',
    author='Waimoku',
    maintainer='Waimoku',
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
