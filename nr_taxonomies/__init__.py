import pathlib
import subprocess


def import_taxonomy(taxonomy_code: tuple = None):
    path = pathlib.Path(__file__).parent.absolute()
    data_directory = path / ".." / "data" / "excel"
    for path in data_directory.iterdir():
        name, suffix = str(path).split("/")[-1].rsplit(".", maxsplit=1)
        if name.startswith("."):
            continue
        if taxonomy_code is None or (name in taxonomy_code):
            subprocess.run(["oarepo", "taxonomies", "import", str(path)])


if __name__ == '__main__':
    import_taxonomy()
