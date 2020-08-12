# A MouseEvent test class

A simple test class that adheres to the [PEP 561](https://mypy.readthedocs.io/en/stable/installed_packages.html#making-pep-561-compatible-packages)
with the `*.py` sources having type annotations, contains an empty `py.typed` and
`setup.py` the "normal items" as well as `package_data` referencing `py.types`
and `zip_safe=False`.

To install use one of the following:

`pip install .`, `pip install -e .` or `pip install git+https://github.com/winksaville/py-mouseevent`

