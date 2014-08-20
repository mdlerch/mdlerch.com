#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Michael Lerch'
SITENAME = 'mdlerch'
SITEURL = 'http://mdlerch.com'

TIMEZONE = 'US/Mountain'
DEFAULT_LANG = 'en'

# RELATIVE_URLS = False
RELATIVE_URLS = True
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = './html5-dopetrope/'

# Blogroll
LINKS = (('about', '/pages/about.html'),
		('projects', '/pages/projects.html'))
		 # ('My edu site', "http://www.math.montana.edu/~lerch"),
		 # ('My github', "https://www.github.com/mdlerch"),)

# Social widget
SOCIAL = (('github', 'https://www.github.com/mdlerch'),
		('twitter', 'http://www.twitter.com/mdlerch'),
		('linkedin', 'http://www.linkedin.com/in/mdlerch'))

STATIC_PATHS = (['CNAME'])

TWITTER_USERNAME = "mdlerch"

DEFAULT_PAGINATION = 10

SUMMARY_MAX_LENGTH = 100

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
