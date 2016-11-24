import logging

from codecats_cv.model import dbExperiences


class Experience:
    def __init__(
            self, category, what, when, title, url, location, flag,
            description, referenceName=None, referenceMail=None, img=None):
        self.category = category
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

    @property
    def asDict(self):
        return self.__dict__


experiences = [
    Experience(
        'work',
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
        'work',
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
    Experience(
        'education',
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
        'education',
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


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    dbExperiences.purge()
    dbExperiences.insert_multiple([e.asDict for e in experiences])
    logging.info(dbExperiences.all())
