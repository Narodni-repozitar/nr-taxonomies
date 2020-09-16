from nr_taxonomies.fetcher import NRTaxonomyFetcher


def test_download_file():
    fetcher = NRTaxonomyFetcher("https://space.techlib.cz/index.php/s/KqHdTLqKXrgst5H/download")
    fetcher.download_file()
    fetcher.extract_tarfile()


def test_import_taxonomy():
    NRTaxonomyFetcher.import_taxonomy("/tmp/taxonomies/languages.xlsx")
