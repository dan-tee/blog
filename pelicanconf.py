#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dan T.'
SITENAME = 'dan-t.de'
SITESUBTITLE = 'A sceptics views on data science, machine learning and startups'
#SITEURL = 'http://dan-t.de'

THEME = 'modernscientist-theme'
SEARCH_BOX = True
X_MIN_READ = True
DISPLAY_CATEGORIES_ON_MENU = False

PATH = 'content'
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['post_stats', 'disqus_static']

DISQUS_SITENAME = 'dan-t-de'
DISQUS_SECRET_KEY = 'tEUe952AoCPMbyeUC226ImgjLSHc4ERTgm3PdPPgpaB7qCOMJe8qRCnQGBfldqjR'
DISQUS_PUBLIC_KEY = 'z96ezZPsruloLlzxYqKTZWbyz5irm52UleMz7kM0DcwxTRcbSYtqF20NLpcoYYWh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Edwin Chen', 'http://blog.echen.me/'),
         ('Andrew Gelman', 'http://andrewgelman.com/'),
         ('Sebastian Raschka', 'http://sebastianraschka.com/blog'),
         ('Erik Bernhardsson', 'http://erikbern.com/'),
         ('Coding Horror', 'http://codinghorror.com/'),
         )

#TWITTER_USER = 'Dan__Tee'

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Dan__Tee'),)

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
