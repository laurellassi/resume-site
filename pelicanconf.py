#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Laurel Lassi'
SITENAME = 'Laurel Lassi Resume'
SITEURL = 'https://github.com/laurellassi/resume-site'

PATH = 'content'

TIMEZONE = 'America/Winnipeg'

DEFAULT_LANG = 'en'

INDEX_SAVE_AS = 'resume.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
PAGE_PATHS = ['pages']  # Ensure Pelican finds your pages

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True