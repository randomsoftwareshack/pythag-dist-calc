from setuptools import setup, find_packages


setup(
    name='pythag-dist-calc',
    version='1.0',
    license='MIT',
    author="randomsoftwareshack",
    author_email='lolimnotputtingmyrealemail@poopmap.net',
    packages=find_packages('pythagdistcalc'),
    package_dir={'': 'pythagdistcalc'},
    url='https://github.com/randomsoftwareshack/pythag-dist-calc',
    keywords='distance formula',
    install_requires=[
          'math',
      ],

)