from setuptools import find_packages, setup

setup(
    name='lib',
    packages=find_packages(include=['lib']),
    version='0.1.0',
    description='My Python library',
    author='Me',
    install_requires=[], 
    setup_requires=['pytest-runner'],
    tests_require=['pytest==8.4.2'],
    test_suite='tests'
)

#running python setup.py pytest is outdated 
#use this instead: pip install --use-pep517 .

#https://medium.com/@parasaroraee/how-to-create-your-own-python-library-a-step-by-step-guide-6a4f151006d0