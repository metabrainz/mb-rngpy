#!/bin/bash

set -e -u

MB_RNGPY_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "$MB_RNGPY_ROOT"

if ! type trang &>/dev/null
then
  echo Error: trang command not found
  echo Please install trang package
  exit 69
fi

################################################################################
echo Updating the schema

cd mmd-schema
git pull origin production
mmd_schema_version=$(git describe --tags --dirty --always)
cd ..
if git diff --name-only | grep -qx mmd-schema
then
  git commit mmd-schema/ \
    -m "Update mmd-schema submodule to $mmd_schema_version"
fi

################################################################################
echo Regenerating the files

make clean
make
git commit mbrng/ musicbrainz_mmd.xsd \
  -m "Regenerate everything with mmd-schema $mmd_schema_version"

################################################################################
echo Testing

pip install --group test
pytest

################################################################################
echo Please review the newly created commits before pushing them.
echo Done

deactivate

# vim: autoindent expandtab filetype=sh softtabstop=2 shiftwidth=2 tabstop=2
