import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name='sqlalchemy_pysqlite3',
  version='0.0.1',
  author='Bjoern Hoehrmann',
  author_email='bjoern@hoehrmann.de',
  description='SQLAlchemy dialect to use pysqlite3 dbapi2',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/hoehrmann/sqlalchemy-pysqlite3',
  packages=setuptools.find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  entry_points = {
    'sqlalchemy.dialects': [
      'sqlite.pysqlite3 = sqlalchemy_pysqlite3:SQLiteDialect_pysqlite3'
    ]
  },
  install_requires=[
    'pysqlite3',
    'sqlalchemy'
  ],
  tests_require=[
    'pysqlite3',
    'sqlalchemy',
    'pytest'
  ]
)
