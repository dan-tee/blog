#!/usr/bin/env bash
cd modernscientist-theme
compass compile
cd ..
echo delete folder /output
rm -r output
make html
make serve