#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mark Huang'
SITENAME = 'Mark Huang'
SITEURL = 'https://markhuang.me'
THEME = './theme/pelican-striped-html5up'
DISQUS_SITENAME = 'codestumps'
PATH = 'content'
TIMEZONE = 'Asia/Singapore'
DEFAULT_LANG = 'en'

# Basic settings
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'General'
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_DATE_FORMAT = '%d %B, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
        )

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/huang.zhenghao/'),
          ('Twitter', 'https://twitter.com/zhenghao1'),
          ('Github', 'https://github.com/zhenghao1'),
          ('LinkedIn', 'https://www.linkedin.com/in/zhenghao1'),)

DEFAULT_PAGINATION = 8
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
PLUGINS = ['neighbors']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
