from setuptools import setup

setup(
    
    name='sites',
    version='1.0',
    long_description=__doc__,
    packages=['sites'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)