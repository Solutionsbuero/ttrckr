from distutils.core import setup
from setuptools import find_packages

setup(
        name='ttrckr',
        version='2.1.0',
        description='Tinfoil Colloquy\'s barcode based Train Tracking.',
        author='72nd, Dinu',
        author_email='message@tinfoil.yoga',
        url='https://tinfoil.yoga',
        packages=find_packages(),
        include_package_data=True,
)
