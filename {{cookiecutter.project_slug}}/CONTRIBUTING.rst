============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

Bug reports
===========

When `reporting a bug <{{cookiecutter.repo_protocol}}://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/issues>`_ please include:

    * Your operating system name and version.
    * Any details about your local setup that might be helpful in troubleshooting.
    * Detailed steps to reproduce the bug.

Documentation improvements
==========================

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

Feature requests and feedback
=============================

The best way to send feedback is to file an issue at {{cookiecutter.repo_protocol}}://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that code contributions are welcome :)

Get Started!
============

Ready to contribute? Here's how to set up `{{ cookiecutter.project_slug }}` for local development.

1. Fork the `{{ cookiecutter.project_slug }}` repo on website.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/{{ cookiecutter.project_slug }}.git

3. Install your local copy into a virtualenv. ::

    $ cd {{ cookiecutter.project_slug }}/
    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -e .[dev]

4. Setup pre-commit, pre-push, commit-msg hooks::

    $ pre-commit install -t pre-commit
    $ pre-commit install -t pre-push
    $ pre-commit install -t commit-msg

5. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

6. Commit your changes and push your branch to remote repo::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

   You should read `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ before doing a commit.

7. Submit a merge(pull) request through the website.

Merge(Pull) Request Guidelines
==============================

If you need some code review or feedback while you're developing the code just make the merge request.

For merging, you should:

1. Include passing tests (run ``tox``).
2. Update documentation when there's new API, functionality etc.
3. Add yourself to ``AUTHORS.rst``.

Deploying
=========

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed.
Then run::

    $ invoke bumpversion patch # possible: auto / major / minor / patch
    $ git push
    $ git push --tags

You should read `Semantic Versioning 2.0.0 <http://semver.org/>`_ before bumping versions.