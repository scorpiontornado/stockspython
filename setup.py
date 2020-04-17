from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '2.0'

setup(
    name='stockspython',
    version=version,
    # install_requires=[
    #     'selenium',
    #     'lxml'
    # ],
    install_requires=requirements,
    author='Nicholas Langford',
    packages=find_packages(),
    include_package_data=True,
    scripts=[
        "stocks_automated.py",
        "stocks.py",
        "test.py",
        "test2.py",
        "test3.py"],
    url='https://github.com/scorpiontornado/stockspython',
    description='A calculator I made for commerce class',
    long_description=long_description,
)
