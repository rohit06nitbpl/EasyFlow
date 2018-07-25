from distutils.core import setup

setup(
    name='EasyFlow',
    version='0.1dev',
    author='Rohit Jain',
    author_email='rohit06nitbpl@gmail.com',
    packages=['easyflow'],
    scripts=['bin/test.py'],
    url='http://pypi.python.org/pypi/EasyFlow/',
    license='LICENSE.txt',
    description='Modular Distributed TensorFlow Framework',
    long_description=open('README.md').read(),
    install_requires=[
        "tensorflow",
        "tensorflow-gpu"
    ],
)
