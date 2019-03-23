from panflute import *


def action(elem, doc):
    if isinstance(elem, Link):
        if elem.url[:4] == 'http':
            # these are valid urls already, no need to process these
            pass
        else:
            elem.url = 'https://xscale.wiki/' + elem.url


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == '__main__':
    main()