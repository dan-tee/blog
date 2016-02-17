#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://dan-t.de'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

GOOGLE_UNIVERSAL_ANALYTICS = 'UA-73903570-1'

PLUGINS += ['disqus_static']
DISQUS_SITENAME = 'dan-t-de'
DISQUS_SECRET_KEY = 'tEUe952AoCPMbyeUC226ImgjLSHc4ERTgm3PdPPgpaB7qCOMJe8qRCnQGBfldqjR'
DISQUS_PUBLIC_KEY = 'z96ezZPsruloLlzxYqKTZWbyz5irm52UleMz7kM0DcwxTRcbSYtqF20NLpcoYYWh'

