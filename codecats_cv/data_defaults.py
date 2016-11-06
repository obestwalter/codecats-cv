SECRET_INIT = ('mike', 'some-password', 'some-secret-key')
"""tuple containing username, password and secret session key"""


class Language:
    def __init__(self, name, flag, level):
        self.name = name
        self.flag = flag
        self.level = level


# TODO move into a db table
class MY:
    NAME = 'Claudia Vivantes'
    EMAIL = 'my.mail@somecorp.com'
    TITLES = (
        ('Master of the Universe', 'http://google.com'),
        ('something else', 'http://yahoo.com'),
        ('IT StudentSupport', None),
    )
    DESCRIPTION = (
        'This is my personal online CV, designed with '
        'Python HTML, CSS and JavaScript.')
    PHONE = '+49 1234 567890'
    ADDRESS = [
        'Street 123',
        'Room 123',
        '12345 City',
        'Germany',
    ]
    SKILLS = [
        'HTML / CSS',
        'Javascript',
        'Python',
        'Advanced elementary Magick!'
    ]
    LANGUAGES = [
        Language('German', 'germany', 100),
        Language('English', 'gb', 89),
        Language('Chinese', 'china', 34),
    ]
