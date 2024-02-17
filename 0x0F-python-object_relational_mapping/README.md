# MySQL in Python #
---
MySQL Python is the MySQL driver for the Python language. It is broken down into two parts, a wrapper library _mysql and the DB-API 2.0 module MySQLdb. All we are concerned with as developers integrating MySQL into our Python scripts is the DB-API module MySQLdb.
The module MySQLdb conforms to the standards set by the Python PEP 249. This is a standard to help promote database development in Python and make integrating with multiple databases much easier.
### Prerequsites ###
1. To install from source, first get the source from the Sourceforge site. 
2. Next make sure you have gcc, make, and the standard suite of compilation tools installed on your computer.
3. Now make sure you have all of the prerequsites installed. You need Python 2.3.4 or greater and its development files (python-devel), the MySQL 4.0 or greater libraries with the development files (mysql-devel), and zlib with it's development files (zlib-devel).
4. If you get any compilation errors you are most likely missing one of these prerequisites. If you installed the prerequisites from source, make sure the compile tools are looking in the correct locations. If you installed from binaries make sure you have the associated -devel files installed. They need to be installed seperately.
---
_The last basic thing that you need to know is that to be able to use the MySQLdb module in any of your packages you just place the ``` import MySQLdb ``` line at the top of your script_
## How to connect your python to your SQL database? ##
Your python scripts should include a connection to the database that you wish to use. All Python DB-API 2.0 modules implement a function ``` module_name.connect ```. This is the function that is used to connect to the database, in our case MySQL (in our case in the tasks it's hbtn_0e_0_usa).
Here is an example of how this works: ``` db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB) ```.
## Getting a Cursor in MySQL Python ##
In order to put our new connnection to good use we need to create a cursor object. The cursor object is an abstraction specified in the Python DB-API 2.0. It gives us the ability to have multiple seperate working environments through the same connection to the database. You can create a cursor by executing the 'cursor' function of your database object: ``` cur = db.cursor() ```. By default the cursor is created using the default cursor class, and there are several different cursor classes that give you different functionality when executing queries.

Reference: https://www.mikusa.com/python-mysql-docs/query.html
---
## Installation: ##
##### Install and activate venv #####

    $ sudo apt-get install python3.8-venv
    $ python3 -m venv venv
    $ source venv/bin/activate ```
##### Install MySQLdb module version 2.0.x & Install SQLAlchemy module version 1.4.x #####
KEEP IN MIND THAT: For installing MySQLdb, you need to have MySQL installed.

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0) ```

``` $ sudo pip3 install SQLAlchemy
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22' ```
```
---
Some resources that may help you if you faced any problem installing anything:
1. No module named SQLAlchemy: https://bobbyhadz.com/blog/python-no-module-named-sqlalchemy
2. No module named SQLdb: https://appuals.com/no-module-named-mysqldb/
Installation for a connector with the server can be done using the command (Linux users):
``` $ pip install mysql-connector-python ```
3. /var/run/mysqld/mysqld.sock' issue: https://stackoverflow.com/questions/11990708/error-cant-connect-to-local-mysql-server-through-socket-var-run-mysqld-mysq
   ```
   sudo apt-get clean
    sudo apt-get update
    sudo apt-get upgrade -f
   ```
   Then you can start running your server using: ``` sudo service mysql start ```.
---
   Now let's start exploring more concpets from ORM, and start knowing more about connecting and unit of work in SQLAlchemy.
### Units of work, what is it? ###
a system that transparently synchronizes all changes in state between objects and their related rows, called a unit of work, as well as a system for expressing database queries in terms of the user defined classes and their defined relationships between each other.

### database driver ###
a piece of software that allows an application to connect and interact with a database system. Programming languages like Python need a special driver before they can speak to a database from a specific vendor. Note that: MySQL’s official documentation uses the term connector instead of driver. Technically, connectors are associated only with connecting to a database, not interacting with it. However, the term is often used for the entire database access module comprising the connector and the driver.
#### Establishing a Connection With MySQL Server ####
MySQL is a server-based database management system. One server might contain multiple databases. To interact with a database, you must first establish a connection with the server. The general workflow of a Python program that interacts with a MySQL-based database is as follows:
1. Connect to the MySQL server.
2. Create a new database.
3. Connect to the newly created or an existing database.
4. Execute a SQL query and fetch results.
5. Inform the database if any changes are made to a table.
6. Close the connection to the MySQL server.
This is a generic workflow that might vary depending on the individual application. But whatever the application might be, the first step is to connect your database with your application.
