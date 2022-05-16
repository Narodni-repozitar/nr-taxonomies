# nr-taxonomies
Module that import taxonomies to National Repository

## Installation

The library is written only for the purposes of the National Repository, and therefore it is not in the PyPi repository
and can only be installed from the source.

## Prerequisites
It is necessary to have
[Invenio-Nusl](https://github.com/Narodni-repozitar/invenio-nusl) installed.

## Quickstart

The library is currently a single-purpose CLI application with a single function and that is the import of taxonomy.
The library will ensure the download of tar archives, its unpacking and import of taxonomies,
which are in xlsx format according to the requirements of
[oarepo-taxonomies](https://github.com/oarepo/oarepo-taxonomies) library.

```bash
invenio nusl taxonomies import [OPTIONS]

Options:
  -u, --url TEXT     Link to the tar archive with all taxonomies
  -t, --target TEXT  Path as string to the directory where taxonomies will be
                     stored

  -s, --suffix TEXT  Suffix of tar archive e.g.: (tax.xz, tar.gz or only tar
  --help             Show this message and exit.

```
All options are optional and the library should work without having to set anything.

## Documentation

Documentation of the taxonomies/controlled vocabularies used for the 'National repository - part documents' is available (for now only in Czech) from the file [vocab_documentation_NRdocs_cz](https://github.com/Narodni-repozitar/nr-taxonomies/blob/taxonomies-for-nr-docs/data/temporary_materials/).
