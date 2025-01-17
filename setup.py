from setuptools import setup

setup(
    name='sqflint',
    version='0.3.2',
    author='Lord Golias',
    author_email='lord.golias1@gmail.com',
    description='Parser, static analyzer and interpreter of SQF (Arma)',
    url='https://github.com/holy-evening-chillers/sqf',
    license='BSD',
    packages=['sqf'],
    include_package_data=True,
    scripts=[
         'sqflint.py'
    ],
    entry_points={
        'console_scripts': [
            'sqflint = sqf.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
    ],
)
