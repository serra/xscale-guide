from panflute import *
from urllib.parse import quote


def action(elem, doc):
    if isinstance(elem, Header):
        if elem.level == 1:
            title_text = tools.stringify(elem)
            url = 'https://xscale.wiki/#' + quote(title_text)
            elem.parent.content.insert(
                elem.index + 1,
                Para(
                    Link(
                        Str('View article on our wiki'),
                        title=title_text,
                        url=url)))


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == '__main__':
    main()