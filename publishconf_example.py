#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'XXX   <-----'
RELATIVE_URLS = False

FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss.xml'

# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

GOOGLE_UNIVERSAL_ANALYTICS = 'XXX    <-----'

PLUGINS += ['disqus_static']
DISQUS_SITENAME = 'XXX   <-----'
DISQUS_SECRET_KEY = 'XXX   <-----'
DISQUS_PUBLIC_KEY = 'XXX   <-----'

