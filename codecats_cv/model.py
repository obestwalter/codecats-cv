from collections import OrderedDict

from codecats_cv.cnf import PATH
from tinydb import TinyDB, Query

db = TinyDB(PATH.DB)
dbExperiences = db.table("experiences")


class ExperienceCategory:
    def __init__(self, title, icon):
        self.title = title
        self.icon = icon

    def __repr__(self):
        return "<%s(%s, %s)>" % (self.__class__.__name__, self.title, self.icon)


# TODO move this into a db table
NAME_CAT_MAP = [
    ("work", ExperienceCategory("WORK EXPERIENCE", "travel")),
    ("education", ExperienceCategory("EDUCATION", "book")),
]


def get_experiences():
    q = Query()
    experiences = OrderedDict()
    for name, cat in NAME_CAT_MAP:
        experiences[cat] = dbExperiences.search(q.category == name)
    return experiences


if __name__ == "__main__":
    print(get_experiences())
