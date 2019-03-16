[![Build Status](https://travis-ci.org/serra/xscale-guide.svg?branch=master)](https://travis-ci.org/serra/xscale-guide)

Scripts to create our XSCALE guide from our wiki.

## Contributing

If you want to contribute to the *content* of the guide,
you should probably head over to the [XSCALE wiki].
Look for tiddlers (wiki pages) with the tag `guide`.
We will regularly update the guide with 
the latest versions of those tiddlers.

This repository is mainly concerned 
with the creation and publication of the guide;
a mostly automated process.
Want to contribute to this? Hack away. Good places to start are 
[`Makefile`](./Makefile) and [import_tiddlers.py](./import_tiddlers.py).
Pull requests with improvements are appreciated.

## How to use

We use Python, [Sphinx] and [Pandoc] for creating our guide.
We suggest you create a virtualenv, but this is optional.

<details>
<code>
virtualenv venv
source venv/bin/activate
</code>
</details>

Before doing anything else, bootstrap the project:

```
make bootstrap
```

At this stage, all dependencies should have been installed in your (virtual) environment.

To build the guide run:

```
make guide
```

This will create a html, epub and pdf version of the guide,
which can be found in `_build/html`, `_build/epub`, and `_build/rinoh` respectively.

## How it works

We download the latest version of our wiki into the `_wiki` folder,
by running `make download`.
Then we import the wiki tiddlers into our guide,
and transform them into .rst format,
by running `make import`.

We combine these imported pages with some custom .rst files 
into our guide using [Sphinx].

---

 [XSCALE wiki]: https://xscsale.wiki
 [Sphinx]: http://www.sphinx-doc.org/
 [Pandoc]: https://pandoc.org/

