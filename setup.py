from setuptools import setup
import os

VERSION = "1.0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-linkify",
    description="Datasette plugin for linkifying columns that contain hyperlinks",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    authors=["Simon Willison", "Kevin Ernst"],
    #url="https://datasette.io/plugins/datasette-linkify",
    url="https://github.com/ernstki/datasette-linkify",
    project_urls={
        "Issues": "https://github.com/ernstki/datasette-linkify/issues",
        "CI": "https://github.com/ernstki/datasette-linkify/actions",
        "Changelog": "https://github.com/ernstki/datasette-linkify/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_linkify"],
    entry_points={"datasette": ["linkify = datasette_linkify"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest"]},
    tests_require=["datasette-linkify[test]"],
)
