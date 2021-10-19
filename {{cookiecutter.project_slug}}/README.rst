{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}

Documentation
=============

{% if cookiecutter.sphinx_docs == "y" %}
`Read the documentation <{{ cookiecutter.sphinx_docs_hosting }}>`_
{% else %}
To use the project::

    import {{ cookiecutter.project_slug }}

{% endif %}

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `HuangKaiHuan/cookiecutter-rrpylibrary`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`HuangKaiHuan/cookiecutter-rrpylibrary`: https://github.com/HuangKaiHuan/cookiecutter-rrpylibrary
