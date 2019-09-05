#!/usr/bin/env python
from datetime import date

AUTHOR = "Bùi Thành Nhân"
SITENAME = "Hi, I'm Nhân"
SITESUBTITLE = "and this is my humble corner on the interwebs."
SITEURL = ""

THEME = "./motherfucking-pelican-theme"

TIMEZONE = "Asia/Ho_Chi_Minh"

DEFAULT_LANG = "en"
TYPOGRIFY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = ["images", "extra"]

EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/favicon.png": {"path": "favicon.png"},
    "extra/404.html": {"path": "404.html"},
    "extra/google3f40dbd543a603fa.html": {"path": "google3f40dbd543a603fa.html"},
}

ARTICLE_PATHS = ["posts"]
ARTICLE_URL = "posts/{slug}/"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"
ARTICLE_LANG_URL = "posts/{slug}-{lang}/"
ARTICLE_LANG_SAVE_AS = "posts/{slug}-{lang}/index.html"

PAGE_PATHS = ["pages"]
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"
PAGE_LANG_URL = "pages/{slug}-{lang}/"
PAGE_LANG_SAVE_AS = "pages/{slug}-{lang}/index.html"

AUTHOR_URL = "author/{slug}/"
AUTHOR_SAVE_AS = "author/{slug}/index.html"

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

DEFAULT_PAGINATION = False

AUTHOR_NAME = "Bùi Thành Nhân"
AUTHOR_SLUG = "nhanb"

THEME_STATIC_PATHS = ["static"]

MENUITEMS = (("Blog", "/"),)

PLUGINS = ["minify"]

MINIFY = {
    "remove_comments": False,
    "remove_all_empty_space": False,
    "remove_optional_attribute_quotes": False,
}

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ATOM = "feeds/atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"

# ========= Theme-specific settings follow =============

MOTHERFUCKING_DEFAULT_THUMB = "images/nhan.jpg"
MOTHERFUCKING_GREETINGS = """
Why hello there, source viewer. Here's a dragon for no particular reason:

       ^                       ^
       |\   \        /        /|
      /  \  |\__  __/|       /  \_
     / /\ \ \ _ \/ _ /      /    \_
    / / /\ \ {*}\/{*}      /  / \ \_
    | | | \ \( (00) )     /  // |\ \_
    | | | |\ \(V""V)\    /  / | || \|
    | | | | \ |^--^| \  /  / || || ||
   / / /  | |( WWWW__ \/  /| || || ||
  | | | | | |  \______\  / / || || ||
  | | | / | | )|______\ ) | / | || ||
  / / /  / /  /______/   /| \ \ || ||
 / / /  / /  /\_____/  |/ /__\ \ \ \ \_
 | | | / /  /\______/    \   \__| \ \ \_
 | | | | | |\______ __    \_    \__|_| \_
 | | ,___ /\______ _  _     \_       \  |
 | |/    /\_____  /    \      \__     \ |    /\_
 |/ |   |\______ |      |        \___  \ |__/  \_
 v  |   |\______ |      |            \___/     |
    |   |\______ |      |                    __/
     \   \________\_    _\               ____/
   __/   /\_____ __/   /   )\_,      _____/
  /  ___/  \____/  ___/___)    \______/
  VVV  V        VVV  V

(ripped off from http://www.retrojunkie.com/asciiart/myth/dragons.htm)
"""

CURRENT_YEAR = date.today().year

FOOTER_TEXT = """
Built with &#9829; and lots of
<a target="_blank" rel="noopener" href="https://caudatfarm.com/">Cầu Đất coffee</a>.
"""
