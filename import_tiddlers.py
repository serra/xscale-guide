import sys
sys.path.insert(0, './PyTiddlyWiki')
from tiddlywiki import TiddlyWiki
from pypandoc import convert_file
import glob
import os

source_dir = './source/_generated/'


def import_tiddlers():
    tw5 = TiddlyWiki.parse_from_html('./_wiki/index.html')
    predicate = lambda t: 'guide' in t.tags
    guide_tiddlers = list(tw5.finditer(predicate))

    for tiddler in guide_tiddlers:
        tiddler.export_to_file(source_dir + tiddler.title + '.md')


def process_tiddlers():
    filters = ['all_relative_links_to_wiki_filter.py']
    input_filenames = glob.glob(source_dir + '*.md')
    for filename in input_filenames:
        outputfilename = os.path.splitext(filename)[0] + '.rst'
        convert_file(
            filename, 'rst', filters=filters, outputfile=outputfilename)


def main():
    import_tiddlers()
    process_tiddlers()


if __name__ == '__main__':
    main()