# mb-rngpy

Python bindings for the MusicBrainz RNG schema. Required by [sir](https://github.com/metabrainz/sir)

## Installation

Development files of both [`libxml2`](http://www.xmlsoft.org/) and
[`libxslt`](http://www.xmlsoft.org/XSLT/) are
required to install [`lxml`](https://lxml.de/) Python package
which is imported by `mb-rngpy`.

If you are on Ubuntu/Debian you can install these via:
```bash
sudo apt-get install libxml2-dev libxslt1-dev
```

Then you can install `mb-rngpy` from [PyPI](https://pypi.org/project/mb-rngpy/) via:
```bash
pip install mb-rngpy
```

It is supported on Python 3 only.

## Community

Join the development community of MusicBrainz at https://community.metabrainz.org/c/musicbrainz/devel

Report issues at https://tickets.metabrainz.org/secure/CreateIssue!default.jspa?pid=10022

## Updating the models

### Requirements

Please install the following programs:

* [Trang](https://github.com/relaxng/jing-trang/releases)

If you are on Ubuntu/Debian you can install these via:
```bash
sudo apt-get install trang
```

Also, note that your pip version should be >= 25.1.0.

### Updating and pushing to Git and PyPI

1. Setup a virtual environment and install dependencies by running `pip install --group dev --group test`.
2. Run `./update.sh` to update schema and regenerate models.
3. Review the generated commits and either open a PR with the changes or push them to master.
4. Create a new GitHub release using the correct tag format. Tags should follow the pattern `2.{MMD_SCHEMA_VERSION}.{PATCH}`, 
   where `PATCH` is incremented by 1 from the previous patch version. When the `MMD_SCHEMA_VERSION` is updated, the PATCH number should be reset to 0.
