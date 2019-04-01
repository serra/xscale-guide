from panflute import *


def action(elem, doc):
    if isinstance(elem, Para):
        text = tools.stringify(elem)
        if '|! Principles' in text or '|! Practices' in text:
            return []


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == '__main__':
    main()