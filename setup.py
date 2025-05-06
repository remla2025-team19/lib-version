from setuptools import setup, find_packages

setup(
    name="lib-version",
    version="0.1.0",
    packages=find_packages(where="versionutil"),
    package_dir={"":"versionutil"},
    python_requires="==3.12.9"
)

