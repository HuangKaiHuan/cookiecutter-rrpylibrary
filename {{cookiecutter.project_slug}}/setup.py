#!/usr/bin/env python

"""The setup script."""

import io
import os
import sys

# Python supported version checks. Keep right after stdlib imports to ensure we
# get a sensible error for older Python versions
if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")


{%- if cookiecutter.use_cython_to_project_code != "y" %}
from setuptools import find_packages, setup
{%- else %}
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools import setup
from setuptools.extension import Extension
{%- endif %}

import versioneer

{%- if cookiecutter.use_cython_to_project_code == "y" %}

sources = ["src"]
exclude = ["__init__.py", "_version.py"]

extensions = []
py_modules = []
for source in sources:
    for dir_path, folder_names, file_names in os.walk(source):
        for file_name in file_names:
            file_path = os.path.join(dir_path, file_name)
            rel_path = os.path.relpath(file_path, "src")
            file_name_no_ext = os.path.splitext(rel_path.replace(os.sep, "."))[0]
            if file_name.endswith((".pyx", ".py")):
                if file_name not in exclude:
                    extension = Extension(
                        file_name_no_ext,
                        sources=[file_path],
                        extra_compile_args=["-Os", "-g0"],
                        extra_link_args=["-Wl,--strip-all"],
                    )
                    extensions.append(extension)
                else:
                    py_modules.append(file_name_no_ext)
{%- endif %}


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
    url="{{ cookiecutter.repo_protocol }}://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass({%- if cookiecutter.use_cython_to_project_code == "y" %}{"build_ext": build_ext}{%- endif %}),
    package_dir={"": "src"},
{%- if cookiecutter.use_cython_to_project_code == "y" %}
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        language_level=3,
        compiler_directives=dict(always_allow_keywords=True),
    ),
    py_modules=py_modules,
    packages=[],
{%- else %}
    packages=find_packages("src"),
{%- endif %}
    zip_safe=False,
)
