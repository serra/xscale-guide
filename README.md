Scripts to create our XSCALE guide from our wiki.

## How to use

```
make download
make guide
```

## Development

We use Python and Sphinx for creating our guide.

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

We use a git submodule, so after your first checkout,
init and update this submodule by doing:

```
git submodule init
git submodule update
```

Hack away. A good place to start is [`Makefile`](./Makefile).
