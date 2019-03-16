Scripts to create our XSCALE guide from our wiki.

## How to use

```
make download
make guide
```

## Development

We use Python, Sphinx and pandoc for creating our guide.
We suggest you create a virtualenv, but this is optional:

```
virtualenv venv
source venv/bin/activate
```

Then, bootstrap the project:

```
make bootstrap
```

Hack away. Good places to start are 
[`Makefile`](./Makefile) and
[import_tiddlers.py](./import_tiddlers.py).
