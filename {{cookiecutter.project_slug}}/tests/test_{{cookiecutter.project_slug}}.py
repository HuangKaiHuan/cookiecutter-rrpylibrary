#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import sample


def test_sample():
    assert sample(True)
    assert not sample(False)
