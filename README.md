# mb-rngpy

Python bindings for the MusicBrainz RNG schema. Required by [sir](https://github.com/metabrainz/sir)

## Installation

You can install `mb-rngpy` from [PyPI](https://pypi.org/project/mb-rngpy/) via:
```bash
pip install mb-rngpy
```

It is supported on Python 2.7 only.

## Community

Join the development community of MusicBrainz at https://community.metabrainz.org/c/musicbrainz/devel

Report issues at https://tickets.metabrainz.org/secure/CreateIssue!default.jspa?pid=10022

## Updating the models

### Requirements

Please install the following programs:

* [Trang](https://github.com/relaxng/jing-trang/releases)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/)

If you are on Ubuntu/Debian you can install these via:
```bash
sudo apt-get install trang python-virtualenv
```

Additional requirements are Python packages:

* [generateDS](http://www.davekuhlman.org/generateDS.html)
* [lxml](https://lxml.de/) (required for generateDS)

These can be installed in virtual environment via:
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Updating the schema

```bash
cd mmd-schema
git pull origin production
cd ..
```

### Generating the files

To update the model to a new schema simply run
```bash
make clean && make
```

It also (re)generates `mbrng/__init__.py` with git-described version.
