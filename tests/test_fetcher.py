import shutil
from pathlib import Path
import os

from nr_taxonomies.fetcher import NRTaxonomyFetcher


class TestNRTaxonomyFetcher:

    def test_init(self):
        fetcher = NRTaxonomyFetcher(
            "https://file-examples-com.github.io/uploads/2017/02/zip_5MB.zip")
        assert fetcher.link == "https://file-examples-com.github.io/uploads/2017/02/zip_5MB.zip"

    def test_download_file(self):
        fetcher = NRTaxonomyFetcher(
            "https://file-examples-com.github.io/uploads/2017/02/zip_5MB.zip")
        target = Path(__file__).parent.absolute()
        path = fetcher.download_file(suffix="zip", path=str(target))
        p = Path(path)
        assert p.is_file()
        os.remove(path)

    def test_extract_tarfile(self):
        target_dir = Path("/tmp/test_nr_taxonomies")
        current_dir = Path(__file__).parent.absolute()
        data_dir = current_dir / "data"
        tar_file_pth = data_dir / "hello.tar.xz"
        if not target_dir.is_dir():
            target_dir.mkdir()
        destination = shutil.copy(tar_file_pth, target_dir)
        NRTaxonomyFetcher._extract_tarfile(destination, "r:xz", target=target_dir)
        with open(str(target_dir/"hello.txt"), "r") as f:
            assert f.read() == "hello world\n"
        shutil.rmtree(target_dir)

    def test_extract_zipfile(self):
        target_dir = Path("/tmp/test_nr_taxonomies")
        current_dir = Path(__file__).parent.absolute()
        data_dir = current_dir / "data"
        tar_file_pth = data_dir / "hello.zip"
        if not target_dir.is_dir():
            target_dir.mkdir()
        destination = shutil.copy(tar_file_pth, target_dir)
        NRTaxonomyFetcher._extract_zipfile(destination, target=target_dir)
        with open(str(target_dir/"hello.txt"), "r") as f:
            assert f.read() == "hello world\n"
        shutil.rmtree(target_dir)
