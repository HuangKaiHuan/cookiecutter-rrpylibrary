========================
Cookiecutter RRPyLibrary
========================

Cookiecutter_ template for a RR Python library.

- repo: https://github.com/HuangKaiHuan/cookiecutter-rrpylibrary.git

Notes:

- Support python3.6+ only
- If you have a application(not a library) you might want to take a look at RRPyApplication_ [no yet complete]

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _RRPyApplication: https://github.com/HuangKaiHuan/cookiecutter-rrpyapplication.git

Features
========

- Formatting with black_
- Import sorting with isort_
- Static typing with mypy_
- Linting with flake8_
- Linting commit message with gitlint_
- Git hooks that run all the above with pre-commit_
- Managing a recorded version number with versioneer_
- Generate changelog from git commit message with gitchanglog_
- Managing dev task with invoke_
- Testing with pytest_
- Managing test environments with tox_
- Generating docs with sphinx_ (optional)
- Continuous Integration with gitlab-ci_ (optional)
- Auto upload package to inter pypi (use gitlab-ci)
- Auto upload document to inter website (use gitlab-ci)

.. _black: https://github.com/psf/black
.. _isort: https://github.com/PyCQA/isort
.. _mypy: https://github.com/python/mypy
.. _flake8: https://github.com/PyCQA/flake8
.. _pre-commit: https://github.com/pre-commit/pre-commit
.. _versioneer: https://github.com/python-versioneer/python-versioneer
.. _gitlint: https://github.com/jorisroovers/gitlint
.. _gitchanglog: https://github.com/vaab/gitchangelog
.. _invoke: https://github.com/pyinvoke/invoke
.. _pytest: https://github.com/pytest-dev/pytest
.. _tox: https://github.com/tox-dev/tox
.. _sphinx: https://github.com/sphinx-doc/sphinx
.. _gitlab-ci: https://docs.gitlab.com/ee/ci/


Quickstart
==========

::

    # Install pipx if cookiecutter are not installed
    python -m pip install --user pipx
    python -m pipx ensurepath

    # Use cookiecutter to create project from this template
    pipx run cookiecutter gh:HuangKaiHuan/cookiecutter-rrpylibrary.git

    # Push initial commit
    cd existing_folder
    git init
    git add .
    git commit -m "First commit"
    git tag 0.1.0 (must 0.1.0)

    # create virtualenv(recommend)
    python -m venv venv
    source venv/bin/activate

    # install dependencies
    pip install -e .[dev]

    # setup pre-commit, pre-push, commit-msg hooks
    pre-commit install -t pre-commit
    pre-commit install -t pre-push
    pre-commit install -t commit-msg

    # Push to remote repo
    create a repo and put it there.
    git remote add origin git@$repo_hosting_domain:$repo_username/$project_name.git
    git push -u origin master

Developing the project
======================

You should read `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ before doing a commit.

To run all the tests, just run::

    tox

To see all the tox environments::

    tox -l

To only build the docs::

    tox -e docs

To run all check::

    pre-commit run -a

Version management
==================

You should read `Semantic Versioning 2.0.0 <http://semver.org/>`_ before bumping versions.

* ``invoke bumpversion patch`` to increase version from `1.0.0` to `1.0.1`.
* ``invoke bumpversion minor`` to increase version from `1.0.0` to `1.1.0`.
* ``invoke bumpversion major`` to increase version from `1.0.0` to `2.0.0`.

At the same time, it will auto update the changelog.

Building and uploading
======================

Before building dists make sure you got a clean build area::

    invoke clean

Note:

    Dirty ``build`` or ``egg-info`` dirs can cause problems: missing or stale files in the resulting dist or
    strange and confusing errors. Avoid having them around.

Then you should check that you got no packaging issues::

    pre-commit run -a

And then you can build the ``sdist``, and if possible, the ``bdist_wheel`` too::

    python setup.py clean --all sdist bdist_wheel

To make a release of the project on PyPI, assuming you got some distributions in ``dist/``, the most simple usage is::

    twine upload --skip-existing dist/*.whl dist/*.gz dist/*.zip

Note:

    `twine <https://pypi.org/project/twine>`_ is a tool that you can use to securely upload your releases to PyPI.
    You can still use the old ``python setup.py sdist bdist_wheel upload`` but it's not very secure - your PyPI
    password will be sent over plaintext.
