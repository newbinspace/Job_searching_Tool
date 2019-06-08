#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `web_scraping` package."""


import unittest
from click.testing import CliRunner

from web_scraping import web_scraping
from web_scraping import cli


class TestWeb_scraping(unittest.TestCase):
    """Tests for `web_scraping` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'web_scraping.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output