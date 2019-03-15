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

Hack away. A good place to start is `makefile`; 
that wil teach how we construct our guide from our wiki.
