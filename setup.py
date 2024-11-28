from setuptools import setup, find_packages

setup(
    name="gigadev",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'faker',
        'pytest>=8.3.3',
    ],
    python_requires='>=3.8',
)
