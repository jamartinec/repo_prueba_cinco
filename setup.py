from setuptools import setup, find_packages

setup(
    name='repo_prueba_cinco',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"": "src"},


)