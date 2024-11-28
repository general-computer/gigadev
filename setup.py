from setuptools import setup, find_packages

setup(
    name="gigadev",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'faker',
    ],
    extras_require={
        'dev': [
            'pytest>=8.3.3',
        ],
    },
)
