SECRET_INIT = ('mike', 'some-password', 'some-secret-key')
"""tuple containing username, password and secret session key"""


class Language:
    def __init__(self, name, flag, level):
        self.name = name
        self.flag = flag
        self.level = level


# TODO move into a db table
class MY:
    NAME = 'YOUR NAME'
    EMAIL = 'your.mail@yourmail.com'
    TITLES = (
        ('Your Studies', 'http://google.com'),
        ('Job Title #1', 'http://yahoo.com'),
        ('Job Title #2', None),
    )
    DESCRIPTION = (
        'This is my personal online CV, designed with '
        'Python HTML, CSS and JavaScript.')
    PHONE = '+12 345 6789 1011'
    ADDRESS = [
        'Street 123',
        'Additional',
        'ZIP City',
        'Country',
    ]
    SKILLS = [
        'Skill #1',
        'Skill #2',
        'Skill #3',
        'Skill #4'
    ]
    LANGUAGES = [
        Language('German', 'germany', 100),
        Language('English', 'gb', 89),
        Language('Chinese', 'china', 34),
    ]
