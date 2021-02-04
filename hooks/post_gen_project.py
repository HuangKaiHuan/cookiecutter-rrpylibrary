#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("docs/authors.rst")

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    if "{{cookiecutter.sphinx_docs}}" != "y":
        shutil.rmtree('docs')

    if "{{cookiecutter.gitlab_ci}}" != "y":
        remove_file(".gitlab-ci.yml")
