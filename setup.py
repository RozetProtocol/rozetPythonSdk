import os
from setuptools import setup, find_packages

datadir = os.path.join('rozet','abis')
datafiles = [(d, [os.path.join(d,f) for f in files])
    for d, folders, files in os.walk(datadir)]

setup(
    name='rozetPySDK',
    version='1.0.3',
    packages=find_packages(),
    include_package_data=True,
    data_files=datafiles,
    url='https://github.com/ShagaleevAlexey/RozetPySDK',
    license='MIT',
    author='Alexey Shagaleev',
    author_email='alexey.shagaleev@yandex.ru',
    description='This is rozetSDK for Rozet Smart Contracts',
    install_requires=[
        'web3',
        'base58',
        'ecdsa',
        'rlp',
        'eth_utils',
        'two1',
        'pycryptodome'
    ]
)
