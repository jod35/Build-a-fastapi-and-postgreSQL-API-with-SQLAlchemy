# Build a REST API with FastAPI, PostgreSQL and SQLAlchemy
FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface. 

SQLAlchemy is a package that makes it easier for Python programs to communicate with databases. Most of the time, this library is used as an Object Relational Mapper (ORM) tool, which automatically converts function calls to SQL queries and translates Python classes to tables on relational databases.

Many web, mobile, geospatial, and analytics applications use PostgreSQL as their primary data storage or data warehouse.

This is code I wrote for the [video](https://youtu.be/2g1ZjA6zHRo)

## How to run the REST API
Get this project from Github
``` 
git clone https://github.com/jod35/Build-a-fastapi-and-postgreSQL-API-with-SQLAlchemy
 
```



### Setting up the database

* Install PostgreSQL and create your user and database

* Change this line in ` database.py ` to 

``` 
engine=create_engine("postgresql://{YOUR_DATABASE_USER}:{YOUR_DATABASE_PASSWORD}@localhost/{YOUR_DATABASE_NAME}",
    echo=True
)
```

### Create a virtual environment
This can be done with 
``` python -m venv env ```

activate the virtual environment with 

``` 
env/bin/activate
```

or 

```
env\Scripts\activate
```



### Install the requirements 

``` 
pip install -r requirements.txt
```

### Create the database
``` python create_db.py ```

## Run the API
``` python main.py ```

## Author 
[Ssali Jonathan](https://github.com/jod35)
