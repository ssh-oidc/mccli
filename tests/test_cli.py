"""Smoke tests for the mccli entry point.

The suite used to contain a broader tests/test_cli.py (only its
__pycache__ survived); until that is restored, these smoke tests at least
prove the package imports and the CLI starts on every supported Python.
"""

from click.testing import CliRunner

from mccli.mccli import cli


def test_cli_help():
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0


def test_cli_version():
    result = CliRunner().invoke(cli, ["--version"])
    assert result.exit_code == 0
