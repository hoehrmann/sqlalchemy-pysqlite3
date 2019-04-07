from pysqlite3 import dbapi2 as sq
from sqlalchemy import create_engine
from sqlalchemy_pysqlite3 import *

def test_compare_versions():
  engine = create_engine('sqlite+pysqlite3:///:memory:')

  alchemy_rows = list(engine.connect().execute(
    'select sqlite_version()'
  ))

  conn = sq.connect(':memory:')
  c = conn.cursor()
  c.execute('select sqlite_version()')

  pysqlite3_rows = c.fetchall()

  assert alchemy_rows[0] == pysqlite3_rows[0]

