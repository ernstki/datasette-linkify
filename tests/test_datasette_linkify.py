import pytest
import markupsafe
from datasette_linkify import render_cell


@pytest.mark.parametrize(
    "input,expected",
    (
        # Ignore empty
        ("", None),

        # Ignore non-match
        ("some stuff, but no links", None),

        # Basic link:
        ("http://example.com",
         '<a href="http://example.com">http://example.com</a>'),

        # HTTPS link:
        ("https://example.com",
         '<a href="https://example.com">https://example.com</a>'),

        # mailto: link
        ("mailto:who@example.com",
         '<a href="mailto:who@example.com">mailto:who@example.com</a>'),

        # URL with query string parts:
        ("https://example.com?q=Hi%20there",
         '<a href="https://example.com?q=Hi%20there">https://example.com?q=Hi%20there</a>'),

        # FIXME: URL with ampersand in query string
        #("https://example.com?q=Hi%20there&r=1",
        # '<a href="https://example.com?q=Hi%20there&r=1">https://example.com?q=Hi%20there&r=1</a>'),

        # URL with anchor
        ("https://example.com#anchor",
         '<a href="https://example.com#anchor">https://example.com#anchor</a>'),

        # evil link
        ("javascript:alert('evil')", None),
    )
)
def test_render_cell(input, expected):
    actual = render_cell(input)
    assert expected == actual
    assert actual is None or isinstance(actual, markupsafe.Markup)
