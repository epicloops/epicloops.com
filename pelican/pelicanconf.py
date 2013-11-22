#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#==============================================================================
# CUSTOM
#==============================================================================
SITE_DESC = '10 Free Loops Emailed Every Week'

#==============================================================================
# METADATA
#==============================================================================
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<p_id>\d{2})_(?P<slug>.*)'
AUTHOR = 'epicloops'
EMAIL = 'epic@epicloops.com'
SITENAME = 'epicloops.com'
SITEURL = '//epicloops.com'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%d %B %Y'

#==============================================================================
# CONTENT PATHS
#==============================================================================
ARTICLE_DIR = 'posts'
ARTICLE_EXCLUDES = ('',)
PAGE_DIR = 'pages'
PAGE_EXCLUDES = ('',)
IGNORE_FILES = [
  '.#*', '.DS_Store'
  ]
STATIC_PATHS = [
  'extra/robots.txt',
  ]
EXTRA_PATH_METADATA = {
  'extra/robots.txt': {'path': 'robots.txt'},
  }

#==============================================================================
# URLs
#==============================================================================
ARTICLE_URL = ''
ARTICLE_SAVE_AS = ''

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = ''
TAG_SAVE_AS = ''

TAGS_URL = ''
TAGS_SAVE_AS = ''

ARCHIVES_URL = ''
ARCHIVES_SAVE_AS = ''

YEAR_ARCHIVE_URL = ''
YEAR_ARCHIVE_SAVE_AS = ''

MONTH_ARCHIVE_URL = ''
MONTH_ARCHIVE_SAVE_AS = ''

DAY_ARCHIVE_URL = ''
DAY_ARCHIVE_SAVE_AS = ''

CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

#==============================================================================
# THEME
#==============================================================================
THEME = 'theme'
THEME_STATIC_DIR = 'static/src'
THEME_STATIC_PATHS = ['static']

#==============================================================================
# TEMPLATES / PAGINATION
#==============================================================================
DIRECT_TEMPLATES = ('index',)
DEFAULT_PAGINATION = False
PAGINATED_DIRECT_TEMPLATES = ('index',)

#==============================================================================
# FEED
#==============================================================================
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#==============================================================================
# SOCIAL
#==============================================================================
TWITTER_HANDLE = 'epic_loops'

#==============================================================================
# CATEGORIES
#==============================================================================
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_CATEGORY = 'Uncategorized'

#==============================================================================
# PLUGINS
#==============================================================================
PLUGIN_PATH = "plugins"
PLUGINS = [
  "assets",
  ]

#==============================================================================
# MISC
#==============================================================================
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

MAILCHIMP = "//epicloops.us6.list-manage1.com/subscribe/post?u=c1397e02455df0aef850100ef&amp;id=b86e6a425e"

