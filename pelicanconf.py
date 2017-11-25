#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Michael Lerch'
SITENAME = 'mdlerch'
SITETITLE = 'mdlerch'
SITEURL = 'http://mdlerch.com'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = False
DEFAULT_PAGINATION = 8

TIMEZONE = 'US/Mountain'
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = "%d %B %Y"

ARTICLE_SAVE_AS = '{date:%Y}/{date:%y-%m}-{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%y-%m}-{slug}.html'

# RELATIVE_URLS = False
RELATIVE_URLS = True
# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

IGNORE_FILES = ['draft*']

THEME = "./themes/Flex/"

ELEGANT_SEARCH = False
ELEGANT_PAGES_DATE = False

# Blogroll
# LINKS = (('about', '/pages/about.html'),
		# ('projects', '/pages/projects.html'))
		 # ('My edu site', "http://www.math.montana.edu/~lerch"),
		 # ('My github', "https://www.github.com/mdlerch"),)

# Social widget
SOCIAL = (('github', 'https://www.github.com/mdlerch'),
		('twitter', 'http://www.twitter.com/mdlerch'),
		('linkedin', 'http://www.linkedin.com/in/mdlerch'),
                ('google','http://plus.google.com/115559038551588800365?rel=author'))

GPLUSID = "115559038551588800365"

STATIC_PATHS = ['CNAME', 'images']

TWITTER_USERNAME = "mdlerch"

SUMMARY_MAX_LENGTH = 50

GOOGLE_ANALYTICS = "UA-54051300-1"

DISQUS_SITENAME = 'mdlerch'

COLOPHON = True
COLOPHON_TITLE = ""
COLOPHON_CONTENT = "<br/>"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
