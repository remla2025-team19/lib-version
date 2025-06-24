from setuptools import find_packages, setup


setup(
    name="lib-version",
    version="0.0.9",
    author="Team 19",
    description="A lightweight utility library that provides version information for your application components.",
    url="https://github.com/remla2025-team19/lib-version",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires="==3.12.9",
)