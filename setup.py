from setuptools import setup, find_packages


setup(
    name='cldfspec',
    version='0.1.0',
    author='Robert Forkel',
    author_email='robert_forkel@eva.mpg.de',
    description='CLDF spec release helpers',
    license='Apache 2.0',
    packages=['cldfspec'],
    entry_points={
        'console_scripts': [
            'cldfspec=cldfspec.__main__:main',
        ],
    },
    python_requires='>=3.6',
    install_requires=[
        'csvw>=1.10',
        'clldutils>=3.5',
        'pycldf',
    ],
)
