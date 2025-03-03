from setuptools import setup, find_packages

setup(
    name='gamesExplorer',
    version='0.0.1',
    description='Paquete para explorar juegos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Maxi',
    author_email='maxifranco1011@ejemplo.com',
    url='https://github.com/MaxiFranco05/gamesExplorer',
    packages=find_packages(),
    install_requires=[
        'requests==2.32.3',
        'lxml==5.3.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)