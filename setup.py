#!/usr/bin/env python
import setuptools
from nekobin import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    dependencies = [_.strip() for _ in f]


setuptools.setup(
    name="nekobin",
    version=__version__,
    description="Nekobin API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU Lesser General Public License v3 (LGPLv3)",
    author="Pokurt",
    author_email="poki@pokurt.me",
    url="https://github.com/OpenRestfulAPI/nekobinpy",
    packages=setuptools.find_packages(exclude="example.py"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=dependencies,
    python_requires=">=3.6",
)
