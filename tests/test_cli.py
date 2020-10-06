from click.testing import CliRunner

from nr_taxonomies.cli import taxonomies


def test_taxonomies_group(app):
    runner = CliRunner()
    result = runner.invoke(taxonomies, ['--help', ])
    assert result.exit_code == 0
    assert "import" in result.output
