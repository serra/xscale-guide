# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = ./source
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "Additional make targets are 'bootstrap', download', 'guide', 'server' and 'rinoh'"

.PHONY: help Makefile

guide: clean rinoh epub html
	cp ./_build/rinoh/XSCALEGuide.pdf ./_build/html/_static/
	cp ./_build/epub/XSCALEGuide.epub ./_build/html/_static/

bootstrap:
	git submodule init
	git submodule update
	pip install -r requirements.txt
	pandoc -v

server:
	sphinx-autobuild $(SOURCEDIR) $(ALLSPHINXOPTS) $(BUILDDIR)/html

download:
	mkdir -p _wiki
	wget https://xscale.wiki/index.html -O _wiki/index.html

import:
	python import_tiddlers.py

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)