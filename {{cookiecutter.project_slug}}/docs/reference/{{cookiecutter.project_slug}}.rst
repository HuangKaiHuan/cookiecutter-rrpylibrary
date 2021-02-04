{{ cookiecutter.project_slug }}
{{ "=" * cookiecutter.project_slug|length }}

.. testsetup::

    from {{ cookiecutter.project_slug }} import *

.. automodule:: {{ cookiecutter.project_slug }}
    :members:
