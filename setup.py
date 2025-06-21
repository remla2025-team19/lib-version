from setuptools import find_packages, setup
import os

# Read version from __init__.py
def get_version():
    init_path = os.path.join(os.path.dirname(__file__), 'src', 'lib_version', '__init__.py')
    with open(init_path, 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip('"').strip("'")
    raise RuntimeError("Unable to find version string.")
setup(
    name="lib-version",
    version=get_version(),
    author="Team 19",
    description="A lightweight utility library that provides version information for your application components.",
    url="https://github.com/remla2025-team19/lib-version",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires="==3.12.9",
)
