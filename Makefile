# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = ./source
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "Custom targets:"
	@echo "  bootstrap   to setup your (virtual) environment for first use"  
	@echo "  download    to download the latest version of the xscale wiki" 
	@echo "  import      to import the content from the downloaded copy of\n" \
          "               the XSCALE wiki into the source of the guide"   
	@echo "  guide       to create html, pdf and epub versions of our guide"
	@echo "  server      to run the guide in sphinx-autobuild mode"
	@echo "  rinoh       to create the pdf version of our guide if you don't\n" \
	      "               have Latex installed"

.PHONY: help Makefile

bootstrap:
	git submodule init
	git submodule update
	pip install -r requirements.txt
	pandoc -v

import:
	python import_tiddlers.py

download:
	mkdir -p _wiki
	wget https://xscale.wiki/index.html -O _wiki/index.html

guide: clean rinoh epub html
	cp ./_build/rinoh/XSCALEGuide.pdf ./_build/html/_static/
	cp ./_build/epub/XSCALEGuide.epub ./_build/html/_static/

server:
	sphinx-autobuild $(SOURCEDIR) $(ALLSPHINXOPTS) $(BUILDDIR)/html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)