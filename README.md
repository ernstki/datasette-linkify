# datasette-linkify

<!--[![PyPI](https://img.shields.io/pypi/v/datasette-linkify.svg)](https://pypi.org/project/datasette-linkify)-->
<!--[![Changelog](https://img.shields.io/github/v/release/ernstki/datasette-linkify?include_prereleases&label=changelog)](https://github.com/ernstki/datasette-linkify/releases)-->
[![Tests](https://github.com/ernstki/datasette-linkify/workflows/Test/badge.svg)](https://github.com/ernstki/datasette-linkify/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ernstki/datasette-linkify/blob/main/LICENSE)

Datasette plugin for rendering links as links, using the
[render_cell plugin hook][0].

This plugin looks for cell values that match a URI-like pattern and converts
the URIs them to clickable links when they are rendered by the Datasette
interface.


## Overview

Columns containing links such as:

    http://example.com
    mailto:somebody@example.com

will be rendered as real `<a href="">` links:

    <a href="http://example.com">http://example.com</a>
    <a href="mailto:somebody@example.com">somebody@example.com</a>


## Known issues

* ampersands (`&`s) in query strings are not currently rendered properly (#1)


## Credits

Based on a fork of Simon Williamson's [dataset-json-html][1] plugin at
revision [af73575][2] (≈1.0.1).


[0]: https://docs.datasette.io/en/stable/plugin_hooks.html#render-cell-value-column-table-database-datasette
[1]: https://github.com/simonw/datasette-json-html
[2]: https://github.com/simonw/datasette-json-html/commit/af735757fc50d4fd86118780f700535b810ff22c
