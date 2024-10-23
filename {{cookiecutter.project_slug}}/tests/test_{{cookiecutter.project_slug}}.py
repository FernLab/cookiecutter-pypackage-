#!/usr/bin/env python

# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam


"""Tests for `{{ cookiecutter.project_slug }}` package."""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else -%}
import unittest
{%- endif %}

import {{ cookiecutter.project_slug }}
{%- if cookiecutter.use_pytest == 'n' %}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
{%- endif %}
