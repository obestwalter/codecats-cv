from setuptools import setup


setup(
    name='codecats-cv',
    version="0.1.0",
    author='Codecats',
    install_requires=open("requirements.txt").readlines(),
    url='https://github.com/obestwalter/codecats-cv',
    use_scm_version=True,
    packages=['codecats_cv'],
    license='Unlicense',
)
