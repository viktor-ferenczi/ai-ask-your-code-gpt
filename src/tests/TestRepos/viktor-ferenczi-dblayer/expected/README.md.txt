# Database Abstraction Layer Generator

Database server support: PostgreSQL

# Installation

* Using pip: ```pip install dblayer```
* From source: ```python setup.py install```

# How it works

## Abstraction layer

Generates source code of a module implementing row classes with slots and a 
single database abstraction layer class. These classes can be used as is or 
extended by inheritance to fit your specific needs. It is also possible to 
extend the row classes to provide properties or helper methods. The generated 
code provides Python IDEs as much information as possible to make code 
completion useful. 

## Lightweight usage

The generated abstraction layer works like an ORM (Object Relational Mapper), 
but without a direct mapping of row instances to the corresponding database 
rows. It makes this approach more lightweight than a full-blown ORM. Database 
sessions and transactions must be initiated explicitly, but there are context 
managers defined to simplify your code.

## Features

Tables, indexes and constraints are defined in a very clean way by just 
writing Python classes. Everything is defined explicitly, no automatic 
discovery of classes. Queries on multiple tables (joins) can also be defined 
in a clean way. Table aliasing is automatic and natural, since all the 
participating tables must be given an unique name in order to build the query 
definition. Highly complex queries can be build up gradually by simple Python 
class inheritance, which helps reducing code redundancy in real world use 
cases.

Constraints are enforced on the database server, not by Python code. It is 
also possible to add record finalization and validation code in Python if 
needed. There is support for defining efficient full text search indexes in a 
very simple way, so searching rows based on their textual contents is easy to 
implement.

# Remarks

## Performance

Most of the SQL is generated at compile time to reduce the runtime overhead as 
much as possible. Despite this it is possible to add runtime conditions, even 
building up complex conditions at runtime, but it will not slow down the 
simple use cases. Literal values are escaped automatically. The abstraction 
layer always returns unicode objects. You can pass str objects as literal 
values, the default encoding is UTF-8 in this case.

## Limitations

The only supported database server is PostgreSQL via the psycopg2 
extension. The generated code works with gevent-psycopg2 as well. 

No support for defining database views, tablespaces and other 
database servers yet. 

No support for inspecting databases (generating the classes defining and 
existing database) yet. 

The unit test coverage is still not 100%.
