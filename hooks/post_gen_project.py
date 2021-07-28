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

    print("""
    ################################################################################
    ################################################################################
        You have successfully created `{{ cookiecutter.project_slug }}`.
    ################################################################################
        You've used these cookiecutter parameters:
    {% for key, value in cookiecutter.items()|sort %}
            {{ "{0:30}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
    {%- endfor %}
    ################################################################################
        To get started run these:
            cd {{ cookiecutter.project_name }}
            
            # create virtualenv(recommend)
            python3 -m venv venv
            source venv/bin/activate
            
            # install dependencies
            pip install -U pip
            pip install -e .[dev]
            
            # auto init the repo by invoke command
            inv init-repo
            
            # Push to remote repo
            git remote add origin git@{{ cookiecutter.repo_hosting_domain }}:{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}.git
            git push -u origin master --tags
    """)
