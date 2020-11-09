import click
from nr_cli import nr

from nr_taxonomies.fetcher import NRTaxonomyFetcher


@nr.group()
def taxonomies():
    pass


@taxonomies.command("import")
@click.option("-u", "--url", "url",
              default="https://space.techlib.cz/index.php/s/KqHdTLqKXrgst5H/download",
              help="Link to the tar archive with all taxonomies",
              type=str
              )
@click.option("-t", "--target", "target", default="/tmp/taxonomies",
              help="Path as string to the directory where taxonomies will be stored", type=str)
@click.option("-s", "--suffix", "suffix", default="tar.xz",
              help="Suffix of tar archive e.g.: (tax.xz, tar.gz or only tar")
def import_taxonomies(url, target, suffix):
    fetcher = NRTaxonomyFetcher(url)
    print("Downloading archive...")
    fetcher.download_file(path=target, suffix=suffix)
    print("Extracting files...")
    fetcher.extract_archive()
    print("Importing taxonomies...")
    fetcher.import_taxonomies()
