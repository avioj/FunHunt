from setuptools import setup

setup(
    name='calculator_back',
    version='0.1',
    long_description=__doc__,
    packages=['src'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', "flask-api"]
)
