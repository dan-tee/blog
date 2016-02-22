#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dan T.'
SITENAME = 'Swan Intelligence'
SITESUBTITLE = 'a practitioners view on data science'
SITELOGO = '/images/black_swan.jpg'
FAVICON_FILENAME = '/images/black_swan.jpg'

#MARKUP = ('md', 'ipynb')
THEME = 'modernscientist-theme'
SEARCH_BOX = True
X_MIN_READ = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Latest', '/index.html'),
             ('All', '/archives.html'),]

PATH = 'content'
TIMEZONE = 'Europe/Berlin'
DEFAULT_DATE_FORMAT = '%d %b %Y'
DEFAULT_LANG = 'en'
TIMEZONE = 'Europe/Berlin'

PLUGIN_PATHS = ['../pelican-plugins', '../pelican-ipynb']
PLUGINS = ['post_stats', 'ipynb']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Edwin Chen', 'http://blog.echen.me/'),
         ('Andrew Gelman', 'http://andrewgelman.com/'),
         ('John Foreman', 'http://www.john-foreman.com/blog'),
         ('Erik Bernhardsson', 'http://erikbern.com/'),
         ('Coding Horror', 'http://codinghorror.com/'),
         )

#TWITTER_USER = 'Dan__Tee'

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/swanint'),)

DEFAULT_PAGINATION = 25
TYPOGRIFY = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
