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
- Protect python codebase with Cython (optional)

.. _black: https://black.readthedocs.io/en/stable/index.html
.. _isort: https://pycqa.github.io/isort/
.. _mypy: https://mypy.readthedocs.io/en/stable/index.html
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _pre-commit: https://pre-commit.com/
.. _versioneer: https://github.com/python-versioneer/python-versioneer
.. _gitlint: https://jorisroovers.com/gitlint/
.. _gitchanglog: https://github.com/vaab/gitchangelog
.. _invoke: https://www.pyinvoke.org/
.. _pytest: https://docs.pytest.org/en/stable/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _sphinx: https://www.sphinx-doc.org/en/master/
.. _gitlab-ci: https://docs.gitlab.com/ee/ci/


Quickstart
==========

::

    # Install pipx if cookiecutter are not installed
    python3 -m pip install --user pipx
    python3 -m pipx ensurepath

    # Use cookiecutter to create project from this template
    pipx run cookiecutter gh:HuangKaiHuan/cookiecutter-rrpylibrary

    # cd to the project root
    cd existing_folder

    # create virtualenv(recommend)
    python3 -m venv venv
    source venv/bin/activate

    # install dependencies
    pip install -U pip
    pip install -e .[dev]

    # auto init the repo by invoke command
    inv init-repo

    # or you can run command step by step
    git init
    git add .
    git commit -m "chore: First commit"
    git tag $your_version
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
* ``invoke bumpversion auto`` to auto increase version.

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
