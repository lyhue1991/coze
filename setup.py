# -*- coding:utf-8 -*-
import re
from pathlib import Path
from setuptools import find_packages, setup, find_namespace_packages

# Settings
FILE = Path(__file__).resolve()
PARENT = FILE.parent  # root directory
README = (PARENT / "README.md").read_text(encoding="utf-8")

def get_version():
    file = PARENT/'coze/__init__.py'
    return re.search(r'__version__="(.*)"', file.read_text(encoding="utf-8"),re.M)[1]


setup(
    name="coze",
    version=get_version(),
    author="lyhue1991",
    author_email="lyhue1991@163.com",
    description="use coze api in python",
    long_description=README,
    install_requires=[           
        #IPython
       ],
    long_description_content_type="text/markdown",
    url="https://github.com/lyhue1991/coze",
    packages=find_namespace_packages(exclude=['data']),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="coze",
    python_requires='>=3.0'
)
