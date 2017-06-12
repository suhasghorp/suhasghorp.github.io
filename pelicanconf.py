#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import platform

def is_windows():
    if platform.system() == 'Windows': return True
    else: return False

def system_path(path):
    """Return path with forward or backwards slashes as necessary based on OS"""
    if is_windows(): return path.replace('/', '\\')
    else: return path.replace('\\', '/')

AUTHOR = u'Suhas Ghorpadkar'
SITENAME = u'QuantMaester'
SITESUBTITLE = u"A blog dedicated to Quant Finance and good-looking graphs."
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# clean urls for pages , trailing slash to support HTTPS
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
# clean urls for articles
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'

TYPOGRIFY  = True

DEFAULT_PAGINATION = 10

MARKUP = ('md','ipynb')
THEME='themes/elegant'

LANDING_PAGE_ABOUT={'title':'I am the watcher on the wall...', 'details':'fkjhgjfgfduhduihgfduhgduhgduighdughdghughd'}

COMMENTS_INTRO='So what do you think? Any comments?'

PLUGIN_PATHS=['plugins']
PLUGINS=['ipynb.markup','sitemap', 'extract_toc', 'post_stats','render_math','better_figures_and_images']
MD_EXTENSIONS = ['toc', 'fenced_code', 'codehilite(css_class=highlight)', 'extra']

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives'))
STATIC_PATHS = ['theme/images', 'images']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
     },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}




