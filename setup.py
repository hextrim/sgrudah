import os
import sys
from codecs import open
from setuptools import setup, find_packages

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

os.chdir(ROOT_DIR)

with open(
    os.path.join(ROOT_DIR, "LONG_DESCRIPTION.rst"), "r", encoding="utf-8") as fo:
    long_description = fo.read()

def strip_comments(l):
    return l.split('#', 1)[0].strip()
 
def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(os.path.join(os.getcwd(), *f)).readlines()]))

setup(
    name="sgrudah",
    version="0.4.0-dev0",
    description="OpenShift API based tool to screen OpenShift projects",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="lo3k/Villian_0x1034",
    author_email="lo3k@hextrim.com",
    url="http://git.hextrim.com/hextrim/sgrudah",
    license="MIT",
    keywords="openshift screen sgrudah",
    packages=find_packages(),
    install_requires=reqs('requirements.txt'),
    python_requires=">=3.6, !=3.7.*",
    project_urls={
        "Bug Tracker": "http://git.hextrim.com/hextrim/sgrudah",
        "Documentation": "http://git.hextrim.com/hextrim/sgrudah",
        "Source Code": "http://git.hextrim.com/hextrim/sgrudah",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
