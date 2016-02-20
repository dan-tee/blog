#!/usr/bin/env bash
make publish
rsync -avc --delete output/ root@dan-t.de:/var/www/blog/