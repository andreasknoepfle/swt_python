from setuptools import setup, find_packages

setup(
    name = 'swtdemo',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires=[
        'setuptools',
    ],
)
