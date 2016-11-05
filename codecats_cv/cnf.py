import logging

import plumbum as plumbum

log = logging.getLogger(__name__)

try:
    from codecats_cv.secrets import DATA
except ImportError:
    DATA = ('dummy-user', 'no-password', 'no-secret-key')
    log.warning("no secret data - using %s instead", DATA)

_HERE = plumbum.LocalPath(__file__).dirname
_PROJECT = _HERE.up()
PKG_NAME = _HERE.basename


class _SECRETS:
    def __init__(self, username, password, secretKey):
        self.USERNAME = username
        self.PASSWORD = password
        self.SECRET_KEY = secretKey


SECRETS = _SECRETS(*DATA)


class NAME:
    STATIC = 'static'
    CONTENT = 'content'
    ROOT = '_root'


class PATH:
    PROJECT = _PROJECT
    SITE = _PROJECT / 'codecats_cv'
    SEMANTIC = SITE / 'semantic'
    STATIC = SITE / NAME.STATIC
    ROOT_FILES = STATIC / '_root'
    VIEW = SITE / 'view'


class STATIC:
    CUSTOM_CSS = 'codecats-cv.css'
    CUSTOM_JS = 'codecats-cv.js'
    CSS = 'semantic/semantic.css'
    CSS_MIN = 'semantic/semantic.min.css'
    JS = 'semantic/semantic.js'
    JS_MIN = 'semantic/semantic.min.js'
