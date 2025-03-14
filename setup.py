import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python_standards",
    version = "0.0.1",
    author = "Christine Malloy",
    author_email = "christinemalloy.engineering@gmail.com",
    description = ("A collection of standards for Python development."),
    license = "BSD",
    keywords = "example documentation tutorial",
    packages=find_packages(where="src"),
    url="https://github.com/christine-malloy/python-standards",
    project_urls={
        "Source": "https://github.com/christine-malloy/python-standards",
    },
    package_dir={"": "src"},
    install_requires=[
        "numpy",
    ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: BSD License",
    ],
    entry_points={
        'console_scripts': [
            'webserver = webserver.main:run',
        ],
    }
)