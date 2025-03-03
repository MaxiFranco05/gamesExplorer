from setuptools import setup, find_packages

setup(
    name='gamesExplorer',
    version='0.0.1',
    description='Paquete para explorar juegos',
    author='Maxi',
    author_email='maxifranco666@ejemplo.com',
    packages=find_packages(),
    install_requires=[
        'requests==2.32.3',
        'lxml==5.3.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
