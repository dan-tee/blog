#!/usr/bin/env bash
source activate root
make publish
rsync -avc --delete output/ root@dan-t.de:/var/www/blog/