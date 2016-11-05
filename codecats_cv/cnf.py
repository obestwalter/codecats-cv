import plumbum as plumbum

_HERE = plumbum.LocalPath(__file__).dirname
_PROJECT = _HERE.up()

print(_HERE.basename)


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
    CSS_CUSTOM = 'codecats-cv.css'
    JS_CUSTOM = 'codecats-cv.js'
    CSS = 'semantic/semantic.css'
    CSS_MIN = 'semantic/semantic.min.css'
    JS = 'semantic/semantic.js'
    JS_MIN = 'semantic/semantic.min.js'
