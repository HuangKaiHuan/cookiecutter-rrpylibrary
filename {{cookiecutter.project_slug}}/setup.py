#!/usr/bin/env python

"""The setup script."""

import io
import os
import sys

# Python supported version checks. Keep right after stdlib imports to ensure we
# get a sensible error for older Python versions
if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")

from setuptools import find_packages, setup

import versioneer


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fh:
        return fh.read()


readme = read("README.rst")
changelog = read("CHANGELOG.rst")

install_requires = [
    # eg: "numpy==1.11.1", "six>=1.7",
]

extras_require = {
    "dev": [
        "black==20.8b1",
        "isort==5.7.0",
        "flake8==3.8.4",
        "mypy==0.800",
        "pre-commit~=2.10.0",
        "pytest==6.2.2",
        "pytest-cov==2.11.1",
        "tox~=3.21.0",
        "versioneer==0.19",
        "gitchangelog==3.0.4",
        "gitlint==0.15.0",
        "invoke==1.5.0",
    ]
}


{%- set license_classifiers = {
    "MIT license": "License :: OSI Approved :: MIT License",
    "BSD license": "License :: OSI Approved :: BSD License",
    "ISC license": "License :: OSI Approved :: ISC License (ISCL)",
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
    "GNU General Public License v3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
} %}

setup(
    author="{{ cookiecutter.full_name.replace("\"", "\\\"") }}",
    author_email="{{ cookiecutter.email }}",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
{%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
{%- endif %}
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="{{ cookiecutter.project_short_description }}",
    install_requires=install_requires,
    extras_require=extras_require,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=readme + "\n\n" + changelog,
    include_package_data=True,
    keywords="{{ cookiecutter.project_slug }}",
    name="{{ cookiecutter.project_slug }}",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="{{ cookiecutter.repo_protocol }}://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
)
