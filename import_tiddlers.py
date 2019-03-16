import sys
sys.path.insert(0, './PyTiddlyWiki')
from tiddlywiki import TiddlyWiki

tw5 = TiddlyWiki.parse_from_html('./_wiki/index.html')

predicate = lambda t: 'guide' in t.tags
guide_tiddlers = list(tw5.finditer(predicate))

for tiddler in guide_tiddlers:
    tiddler.export_to_file('./_wiki/' + tiddler.title + '.rst')
