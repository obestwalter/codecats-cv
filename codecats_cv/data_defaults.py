SECRET_INIT = ('mike', 'some-password', 'some-secret-key')
"""tuple containing username, password and secret session key"""


class Language:
    def __init__(self, name, flag, level):
        self.name = name
        self.flag = flag
        self.level = level


class ExperienceCategory:
    def __init__(self, title, icon, experiences):
        self.title = title
        self.icon = icon
        self.experiences = experiences


class Experience:
    def __init__(self, what, when, title, url, location, flag, description,
                 referenceName=None, referenceMail=None, img=None):
        self.what = what
        self.when = when
        self.title = title
        self.url = url
        self.location = location
        self.flag = flag
        self.description = description
        self.referenceName = referenceName
        self.referenceMail = referenceMail
        self.img = img


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
    EXPERIENCE = [
        ExperienceCategory('WORK EXPERIENCE', 'travel',
            [
                Experience(
                    'codecats',
                    '2015 - TODAY',
                    'Head of Project & Co-Founder',
                    'http://codecats.io',
                    'Friedrichshafen, Germany',
                    'germany',
                    'Some longwinded description what I did or do.',
                    'Max Muster',
                    'max@muster.com',
                    'cc_logo.png'),
                Experience(
                    'Bla Bla',
                    'Past - Present',
                    'Master of Desaster',
                    'http://codecats.io',
                    'Friedrichshafen, Germany',
                    'germany',
                    'Some longwinded description what I did or do.',
                    'Max Muster',
                    'max@muster.com',
                    'zu_logo.png'),
            ]
        ),
        ExperienceCategory('EDUCATION', 'book',
            [
                Experience(
                    'codecats',
                    '2015 - TODAY',
                    'Head of Project & Co-Founder',
                    'http://codecats.io',
                    'Friedrichshafen, Germany',
                    'germany',
                    'Some longwinded description what I did or do.',
                    'Max Muster',
                    'max@muster.com',
                    'cc_logo.png'),
                Experience(
                    'Bla Bla',
                    'Past - Present',
                    'Master of Desaster',
                    'http://codecats.io',
                    'Friedrichshafen, Germany',
                    'germany',
                    'Some longwinded description what I did or do.',
                    'Max Muster',
                    'max@muster.com',
                    'zu_logo.png'),
            ]
        )
    ]
