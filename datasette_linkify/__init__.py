import re
import markupsafe
from datasette import hookimpl

legal_chars = ['-', '~', '.', '%', r'\w']

# ref: https://datatracker.ietf.org/doc/html/rfc3986.html
delims = [
    # gen - delims
    r"\[", r"\]", ":", "/", "?", "#", "@",
    # sub - delims
    "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "="
]

uri_re = re.compile(
    r"((?:mailto|https?):[{legal_chars}{delims}]+)\b".format(
        delims="".join(delims),
        legal_chars="".join(legal_chars)
    )
)


@hookimpl
def render_cell(value):
    if not isinstance(value, str):
        return None

    uris = uri_re.findall(value)

    if not uris:
        return None

    for u in uris:
        value = value.replace(
            u,
            "<a href=\"{href}\">{href}</a>".format(href=markupsafe.escape(u))
        )

    return markupsafe.Markup(value)
