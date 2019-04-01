import sys
sys.path.insert(0, './PyTiddlyWiki')
from tiddlywiki import TiddlyWiki
from pypandoc import convert_file
import glob
import os

source_dir = './source/_generated/'


def import_tiddlers(predicate):
    tw5 = TiddlyWiki.parse_from_html('./_wiki/index.html')
    guide_tiddlers = list(tw5.finditer(predicate))

    for tiddler in guide_tiddlers:
        tiddler.export_to_file(source_dir + tiddler.title + '.md')


def process_tiddlers():
    filters = glob.glob('./filters/*.py')
    input_filenames = glob.glob(source_dir + '*.md')
    for filename in input_filenames:
        outputfilename = os.path.splitext(filename)[0] + '.rst'
        convert_file(
            filename, 'rst', filters=filters, outputfile=outputfilename)


def main():
    tagged_guide = lambda t: 'guide' in t.tags
    import_tiddlers(tagged_guide)

    predicate = lambda t: t.title.startswith('metrics')
    import_tiddlers(predicate)

    process_tiddlers()


if __name__ == '__main__':
    main()