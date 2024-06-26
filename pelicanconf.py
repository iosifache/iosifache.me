AUTHOR = "George-Andrei Iosif"
SITENAME = "@iosifache"
SITEURL = ""

PATH = "./content"

TIMEZONE = "Europe/Bucharest"

DEFAULT_LANG = "en"
THEME = "./theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGINS = ["yaml_metadata", "linkclass"]

FAVICON = "theme/images/favicon.png"


# For pelican-linkclass

LINKCLASS = (
    ("EXTERNAL_CLASS", "external-links"),
    ("INTERNAL_CLASS", "internal-links"),
)


# Static folders

STATIC_PATHS = ["feeds"]
