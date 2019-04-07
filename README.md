# pysqlite3-sqlalchemy-dialect

This module registers an SQLAlchemy dialect for `sqlite` that uses
`pysqlite3.dbapi2` instead of `pysqlite2.dbapi2` or `sqlite3.dbapi2`.
When `pysqlite3` is linked to a more recent version of SQLite3 than
the system library, this allows you to use the newer version together
with SQLAlchemy.

It would also be possible to do by passing a `module` parameter to 
`create_engine`, but that option is not always available.

## Installation

```bash
pip install sqlalchemy-pysqlite3
```

## Synopsis

```python
from sqlalchemy import create_engine
engine = create_engine('sqlite+pysqlite3:///:memory:', echo=True)
''')]
```
