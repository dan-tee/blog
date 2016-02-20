#!/usr/bin/env bash
cd modernscientist-theme
compass compile
cd ..
make html
make serve