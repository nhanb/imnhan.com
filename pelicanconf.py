#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bùi Thành Nhân'
SITENAME = u'Nhanb'
SITEURL = ''

THEME=u'/home/nhanb/dev/pelican-octopress-theme'

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = ['images']

# Copy static files to output
FILES_TO_COPY = (('extra/CNAME', 'CNAME'),
                 ('extra/README.markdown', 'README.markdown'),
                 ('extra/favicon.ico', 'favicon.ico'),
                 ('extra/cal.html', 'calendar/index.html')
                 )

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}/index.html'

PAGE_URL = ('pages/{slug}/')
PAGE_SAVE_AS = ('pages/{slug}/index.html')
PAGE_LANG_URL = ('pages/{slug}-{lang}/')
PAGE_LANG_SAVE_AS = ('pages/{slug}-{lang}/index.html')

AUTHOR_URL = ('author/{slug}/')
AUTHOR_SAVE_AS = ('author/{slug}/index.html')

CATEGORY_URL = ('category/{slug}/')
CATEGORY_SAVE_AS = ('category/{slug}/index.html')

TAG_URL = ('tag/{slug}/')
TAG_SAVE_AS = ('tag/{slug}/index.html')

DEFAULT_PAGINATION = 10

#THEME = "/home/nhanb/Dropbox/dev/pelican-simplicity-theme"

GITHUB_USERNAME = "nhanb"
FACEBOOK_USERNAME = "thanhnhanb"

AUTHOR_NAME = "Bùi Thành Nhân"
AUTHOR_SLUG = "nhanb"

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
          #('Another social link', '#'),)

## Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/')
         #)
