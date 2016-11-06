import itertools
from setuptools import setup

# TODO figure out best way to integrate tests - see http://pythonhosted.org/pytest-runner/


def get_extra_dependencies():
    extras = {
        'tests': ['tox', 'flake8', 'pytest', 'pytest-watch'],
        'docs': ['mkdocs', 'mkdocs-material']}
    extras.update(dict(all=list(itertools.chain(*extras.values()))))
    return extras


setup(
    name='codecats-cv',
    version="0.1.0",
    author='Codecats',
    setup_requires=['setuptools_scm', 'pytest-runner'],
    install_requires=open("requirements.txt").readlines(),
    url='https://github.com/obestwalter/codecats-cv',
    use_scm_version=True,
    packages=['codecats_cv'],
    extras_require=get_extra_dependencies(),
    license='Unlicense',
)
