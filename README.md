# mb-rngpy

## Generating the files

There are two things that need to be set up before file generation:

1. Python environment with [generateDS](http://www.davekuhlman.org/generateDS.html) installed in it.
2. [jing-trang](https://github.com/relaxng/jing-trang) JAR file copied into the ./bin directory in the root of the project. It can be downloaded from https://code.google.com/archive/p/jing-trang/downloads.

After things above are done make sure that `mmd-schema` submodule is pointing to the right version and run:

```bash
$ make mbrng/models.py
```

This should update all the files.
