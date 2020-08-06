from setuptools import setup, find_packages
from codecs import open

# with open("requirements.txt") as f:
#     required = f.read().splitlines()
required = ['click==7.1.1', 'connexion==2.7.0', 'continuous-threading==1.1.1', 'Flask==1.1.2', 'flask-marshmallow==0.12.0', 'Flask-SQLAlchemy==2.4.1', 'marshmallow==3.6.0', 'marshmallow-sqlalchemy==0.23.0', 'pyicloud==0.9.7', 'requests==2.23.0', 'SQLAlchemy==1.3.17', 'swagger-ui-bundle==0.0.6', 'voluptuous==0.11.7', 'voluptuous-serialize==2.3.0', 'tox==3.18.1']

with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="brainless",
    version="0.1",
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
    python_requires="=3.8",
    keywords=["todoist", "brainless", "productivity"],
)