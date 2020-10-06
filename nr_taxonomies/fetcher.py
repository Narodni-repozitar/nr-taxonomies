import subprocess
import tarfile
import uuid
import zipfile
from pathlib import Path

import requests


class NRTaxonomyFetcher:

    def __init__(self, link: str):
        self.link = link
        self.path = ""
        self.taxonomy_dir = ""

    def download_file(self, url=None, path="/tmp/taxonomies/", suffix="tar.xz"):
        if not url:
            url = self.link
        p = Path(path)
        if not p.is_dir():
            p.mkdir()
        local_filename = str(uuid.uuid4()) + "." + suffix
        path = p / local_filename
        # NOTE the stream=True parameter below
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    # if chunk:
                    f.write(chunk)
        self.path = str(path)
        return self.path

    def extract_archive(self, path: str = None):
        if not path:
            path = self.path
        if path.endswith("tar.gz"):
            target = self._extract_tarfile(path, "r:gz")
        elif path.endswith("tar.xz"):
            target = self._extract_tarfile(path, "r:xz")
        elif path.endswith("tar"):
            target = self._extract_tarfile(path, "r:")
        elif path.endswith("zip"):
            target = self._extract_zipfile(path)
        else:
            raise Exception("This is not tar or zip archive")
        self.taxonomy_dir = target

    @staticmethod
    def _extract_tarfile(path, suffix, target="/tmp/taxonomies"):
        p = Path(target)
        if not p.is_dir():
            p.mkdir()
        tar = tarfile.open(path, suffix)
        tar.extractall(path=target)
        tar.close()
        tar_p = Path(path)
        tar_p.unlink(missing_ok=True)
        return target

    @staticmethod
    def _extract_zipfile(path, target="/tmp/taxonomies"):
        p = Path(target)
        if not p.is_dir():
            p.mkdir()
        with zipfile.ZipFile(path, "r") as zf:
            zf.extractall(target)
        tar_p = Path(path)
        tar_p.unlink(missing_ok=True)
        return target

    def import_taxonomies(self, dir_=None):
        if not dir_:
            dir_ = self.taxonomy_dir
        p = Path(dir_)
        for path in p.iterdir():
            if str(path).endswith("xlsx"):
                self.import_taxonomy(path)

    @staticmethod
    def import_taxonomy(path):
        subprocess.run(["invenio", "taxonomies", "import", str(path)])
