from setuptools import setup, find_packages
from codecs import open

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="brainless",
    version="0.2",
    license="MIT",
    url="https://github.com/joaovbmdias/brainless",
    description="An automatic task scheduler for Todoist",
    long_description=long_description,
    maintainer="joaovbmdias",
    maintainer_email=" ",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(include=["src*"]),
    install_requires=required,
    python_requires=">=3.6.0",
    keywords=["todoist", "brainless", "productivity"],
)